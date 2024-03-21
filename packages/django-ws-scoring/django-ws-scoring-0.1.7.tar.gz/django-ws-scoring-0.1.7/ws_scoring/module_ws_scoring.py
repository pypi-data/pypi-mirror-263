import numpy as np
import pandas as pd
from django.db.models import When, Value, Case, DecimalField
from django_pandas.io import read_frame


class ManipulateQuerySet:
    def __init__(self, queryset, user_history, field_weight_dict):
        self.queryset = queryset
        self.user_history = user_history
        self.field_weight_dict = field_weight_dict

    def preprocess_user_history(self):
        # Assuming self.user_history is a list of dictionaries or a similar structure that can be read into a DataFrame
        user_history_df = read_frame(self.user_history)

        if user_history_df.empty:
            return user_history_df  # Return the empty DataFrame early

        # Sort by 'created_at' in descending order
        user_history_df = user_history_df.sort_values(by='created_at', ascending=False)

        # Drop duplicate entries based on 'keyword_search' and 'location_search'
        user_history_df = user_history_df.drop_duplicates(subset=['keyword_search', 'location_search', 'kldb'],
                                                          keep='first')

        # Calculate the max 'created_at' for normalization
        max_created_at = user_history_df['created_at'].max()

        # Calculate the days difference from the max 'created_at'
        user_history_df['days_diff'] = (max_created_at - user_history_df['created_at']).dt.days

        # Assign rows to groups based on 'days_diff'
        user_history_df['group'] = pd.cut(
            user_history_df['days_diff'],
            bins=[-np.inf, 7, 31, np.inf],
            labels=['group1', 'group2', 'group3'],
            right=False
        )

        # Calculate frequency weights independently
        valid_keyword_searches = user_history_df['keyword_search'][user_history_df['keyword_search'].notnull()
                                                                   & (user_history_df['keyword_search'] != '')]
        valid_location_searches = user_history_df['location_search'][user_history_df['location_search'].notnull()
                                                                   & (user_history_df['location_search'] != '')]
        keyword_frequency = valid_keyword_searches.value_counts()
        location_frequency = valid_location_searches.value_counts()

        # Map the frequencies back to the original dataframe
        user_history_df['keyword_frequency_weight'] = user_history_df['keyword_search'].map(keyword_frequency).fillna(0)
        user_history_df['location_frequency_weight'] = user_history_df['location_search'].map(
            location_frequency).fillna(0)

        # Calculate a combined frequency weight by summing keyword and location frequency weights
        user_history_df['total_weight'] = user_history_df['keyword_frequency_weight'] + user_history_df[
            'location_frequency_weight']
        # user_history_df['total_weight'] = user_history_df['frequency_weight']  # Adjust this calculation as needed

        # Filter and select rows based on group assignment
        group1_df = user_history_df[user_history_df['group'] == 'group1']
        group2_df = user_history_df[user_history_df['group'] == 'group2'].sort_values(by='total_weight',
                                                                                      ascending=False).head(3)
        group3_df = user_history_df[user_history_df['group'] == 'group3'].sort_values(by='total_weight',
                                                                                      ascending=False).head(1)

        # Concatenate the selected rows from each group
        final_df = pd.concat([group1_df, group2_df, group3_df])

        # Sort the final_df by 'created_at' in descending order to ensure it's in the correct order
        # This step is crucial if the concatenation disrupts the order you're expecting for applying the weight factor
        final_df = final_df.sort_values(by='created_at', ascending=False)

        # Apply a depreciating factor to each row in final_df
        starting_weight = 1.0
        depreciation_rate = 0.75  # Adjust this as needed

        # Calculate the number of rows in final_df
        num_rows = len(final_df)

        # Generate a list of depreciating factors for each row
        depreciating_factors = [starting_weight * (depreciation_rate ** i) for i in range(num_rows)]

        # Assign the generated depreciating factors to a new column 'weight_factor' in final_df
        final_df['weight_factor'] = depreciating_factors
        # Now, final_df includes a 'weight_factor' column with depreciating values for each row, ready to return
        return final_df

    def get_scores_map(self):
        # Preprocess user history first
        user_history_df = self.preprocess_user_history()
        # Convert queryset to DataFrame
        df = read_frame(self.queryset)

        # Initialize relevancy score column
        df['relevancy_score'] = 0

        # Prepare the weight data
        field_weight_df = pd.DataFrame(list(self.field_weight_dict.items()), columns=['field', 'weight'])

        # Extract location weight
        location_weight = field_weight_df.loc[field_weight_df['field'] == 'location', 'weight'].values[0]

        # Extract keyword weights
        keyword_weights = field_weight_df[~field_weight_df['field'].isin(['location', 'kldb'])].set_index('field')['weight'].to_dict()

        kldb_weight = field_weight_df.loc[field_weight_df['field'] == 'kldb', 'weight'].values[0]

        # Process each preprocessed user search
        df['lower_location'] = df['location'].astype(str).str.lower()
        for field in keyword_weights.keys():
            if field in df.columns:
                df[f'lower_{field}'] = df[field].astype(str).str.lower()

        df['kldb_score'] = 0

        # Vectorized operation for keyword search
        for _, user_search in user_history_df.iterrows():
            current_factor = user_search['weight_factor']
            if user_search.keyword_search:
                keyword = user_search.keyword_search.lower()
                for key, weight in keyword_weights.items():
                    # Check if the user's keyword_search matches the current dictionary keyword
                    keyword_mask = df[f'lower_{key}'].str.contains(keyword, case=False)
                    df['relevancy_score'] += keyword_mask * weight * current_factor

            if user_search.location_search:
                location = user_search.location_search.lower()
                location_match = df['lower_location'].str.contains(location, case=False)
                df['relevancy_score'] += location_match * location_weight * current_factor

            if user_search.kldb:
                # Filter for rows where the first two digits match
                mask = df['kldb'].str.startswith(user_search.kldb[:2])
                # For rows that pass the filter, calculate continuous match score
                if mask.any():
                    def calculate_continuous_match(row):
                        score = 0
                        for i in range(2, 5):
                            if row['kldb'][i:i + 1] == user_search.kldb[i:i + 1]:
                                score += 1
                            else:
                                break
                        return score

                    df.loc[mask, 'kldb_score'] = df[mask].apply(calculate_continuous_match, axis=1)

                df['relevancy_score'] += df['kldb_score'] * kldb_weight * current_factor

        # Drop the temporary lower case columns after use
        df.drop(columns=[f'lower_{field}' for field in keyword_weights.keys()] + ['lower_location', 'kldb_score'],
                inplace=True)

        df = df[df['relevancy_score'] > 0]

        # Create a mapping of IDs to scores
        scores_map = df.set_index('id')['relevancy_score'].to_dict()

        return scores_map

    def calculate_relevancy(self):
        scores_map = self.get_scores_map()
        # Prepare a Case statement for annotating queryset
        cases = [When(id=key, then=Value(val)) for key, val in scores_map.items()]

        annotated_qs = self.queryset.annotate(
            relevancy_score=Case(*cases, default=Value(0), output_field=DecimalField())
        ).order_by('-relevancy_score')

        return annotated_qs
