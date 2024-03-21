
import pandas as pd
import numpy as np
from NeuronsMemoryTestPipeline import MRT_text_processing

def process_recall(df, filter_task, model, group=['group_id']):
    """ Prepares the data, process it using text cleaning module, calculates free recall scores per group, including average position and average recall %.
    Args:
        df: dataframe with data from Jatos and identified MRT module plus task_name
        group (list): group by list that provides filter for grouping dataset
    Returns:
        df: updated data frame with the score column
    """

    df = df.copy()
    df_cleaned = pd.DataFrame()
    corrected_entries = pd.DataFrame()
    original_corrected = pd.DataFrame()
    not_mentioned = pd.DataFrame()
    for group in sorted(df.group_id.unique().tolist(), reverse=False):
        print(f'\n\n *** Group ID: {group} ***')
        df_group = df[df.group_id == group].copy()

        #preparing the list of brand used as template for aitext
        mask = (df_group['expected_response'].str.endswith(('Video', 'Image')) | df_group['expected_response'].notna())
        total_stimulus = df_group[mask]['expected_response'].dropna().unique().tolist()
        mask = ~(df['expected_response'].str.endswith(('Video', 'Image')) | df['expected_response'].isna())
        target_brands = df_group.loc[mask, 'expected_response'].dropna().unique().tolist()
        print(f'\nBRANDS used in the project for group {group}:')
        for brand in sorted(target_brands):
            print('  ', brand)

        #preparing the list of responses and dataframe for processing 
        df_group = df_group.loc[(df_group['task_name'] == filter_task) & (df_group['trial_name'].str.startswith('R-'))]
        responses_to_clean = df_group.given_response_label_presented.dropna().unique().tolist()
        df_group, corrected_counts, corrected_df = MRT_text_processing.clean_free_recall(df_group, target_brands, responses_to_clean, model)
    
        corrected_df['group_id'] = group

        corrected_entries = pd.concat([corrected_entries, corrected_counts], axis=0, ignore_index=True)
        original_corrected = pd.concat([original_corrected, corrected_df], axis=0, ignore_index=True)

        #score calculation
        df_group['position'] = df_group['trial_name'].apply(lambda x: int(x.split('-')[-1]))
        df_group = df_group[df_group.recalled_brand.isin(target_brands)]
        df_cleaned = pd.concat([df_cleaned, df_group], axis=0, ignore_index=True)
        not_there = pd.DataFrame({'recalled_brand': list(set(target_brands) - set(original_corrected['corrected'].unique()))})
        not_there['group_id'] = group
        not_mentioned = pd.concat([not_mentioned, not_there], axis=0, ignore_index=True)
    original_corrected = original_corrected.sort_values(['group_id', 'method', 'original']).reset_index(drop = True)
    return df_cleaned, corrected_entries, original_corrected, not_mentioned


def compute_scores(df_given, no_recall, group = ['group_id', 'project_identifier', 'task_name', 'recalled_brand','total_participants']):
    """ Calculates: Average % , Average position, Average Log score based on position
    Args:
        df (dataframe): processed data frame with cleaned text
        no_recall (dataframe): dataset with brands that were not mentioned
    Returns:
        dataframe: updated dataframe with the scores columns
    """
    df = df_given.copy()
    df['position_mean'] = df.groupby(group, observed=False)['position'].transform('mean')
    df['brand_count'] = df.groupby(group, observed=False)['position'].transform('count')
    df['recall_%'] = df['brand_count'] / df['total_participants'] * 100
    df['mrt_score_freerecall'] = df.apply(lambda row: (1 / (np.log(row['position'] + 1))) * (row['recall_%']), axis=1)
    df = df[group + ['brand_count', 'position_mean', 'recall_%', 'mrt_score_freerecall']].copy()
    df['mrt_score_freerecall'] = df.groupby(group + ['brand_count', 'position_mean', 'recall_%'], observed = False)['mrt_score_freerecall'].transform('mean')
    df = np.round(df, 2)

    columns_to_fill_zeros = ['brand_count', 'position_mean', 'recall_%', 'mrt_score_freerecall', 'total_participants' ]
    same_cols =['project_identifier', 'task_name']
    no_recall[same_cols] = df[same_cols]
    no_recall[columns_to_fill_zeros] = 0
    df = pd.concat([df, no_recall], axis=0, ignore_index=True)
    df.sort_values(['group_id','mrt_score_freerecall'], ascending=[True, False], inplace=True)
    df = df.drop_duplicates()
    df = df.reset_index(drop= True)
    return df
