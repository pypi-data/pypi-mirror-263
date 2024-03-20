import os
import sys
import json
import pandas as pd


# DEFINE ALL MODULES ***************************
def tabulate_group(df,list):
    """Creates a tabulate of the given columns Parameters
    ----------
    df: Dataframe we want to rename its columns
    list:List of the columns we want to group by with
    Returns
    -------
    The tabulate
    """
    return(df.groupby(list).size().reset_index())
    
def filter_conditions(df):
    """Flag data by reaction_time constrains per participant, per module
    df: Dataframe that contains participants, module and reaction time

    Returns: return position of the data based on the filter as Good, Above or Below
    """
    module_name = df['module_name']
    reaction_time = df['reaction_time']

    if module_name in ['FRT-C_Em', 'FRT-C_Em-Pre', 'FRT-C_Em-Post']:
        if reaction_time < 350:
            return "Below"
        elif reaction_time > 2500:
            return "Above"
        else: return "Good"

    elif module_name == 'FRT-C_Mo':
        if reaction_time < 300:
            return "Below"
        elif reaction_time > 2500:
            return "Above"
        else: return "Good"
        
    elif module_name == 'FRT-B_Me':
        if reaction_time < 400:
            return "Below"
        elif reaction_time > 4000:
            return "Above"
        else: return "Good"


def check_files(args):
    """Checks if the provided files are correct and in appropriate order
    args: list of files entered in the system
    Returns: 
        dataframe: jatos file
        string: project name
    """
    try: 
        upload_jatos(args[0])

    except FileNotFoundError:
        print(f'********** JATOS file "{args[0]}" not found. Please make sure the file exists and try again.**********\n')
        sys.exit(1)
    
    except Exception as e:
        print(f'********** Error uploading JATOS file, please enter it before any Demographic File: {e} **********\n')
        sys.exit(1)


def upload_jatos(file):
    """Checks if the provided jatos file exists, checks its extention 
    and uploads it as DF using either TXT or SCV reading methods
    file: identified jatos file, entered in the system
    Returns: 
        dataframe: jatos file
    """
    try:
        if os.path.splitext(file)[1] == '.txt':     # Load data from the jatos file (txt. file)
            l_d = []
            with open(file, encoding='UTF-8') as f:
                for line in f:
                    l_d.append(json.loads(line))

            new_l_d = []
            for item in l_d:
                if isinstance(item, dict):
                    new_l_d.append(item)
                elif isinstance(item, int):
                    continue
                else:
                    new_l_d.extend([b for b in item if b is not None])
            l_d = new_l_d

            for i in range(len(l_d)):
                d = l_d[i]
                if 'responses' in d.keys():
                    d.update(json.loads(d['responses']))
                    l_d[i] = d
            df_jatos = pd.DataFrame(l_d)
            df_jatos['behavioral_task_duration_dt'] = pd.to_timedelta(df_jatos['behavioral_task_duration'])
            df_jatos['behavioral_task_duration_minutes'] = df_jatos['behavioral_task_duration_dt'].dt.total_seconds() / 60

        else:                                       # Load data from the jatos file (csv. file)
            df_jatos = pd.read_csv(file, low_memory=False)
            df_jatos['participant_id'] = df_jatos['participant_id'].str.strip()
            df_jatos['participant_id'] = df_jatos['participant_id'].astype(str)
            df_jatos['reaction_time'] = pd.to_numeric(df_jatos['reaction_time'], errors= 'coerce')
        return df_jatos

    except:
        print(f'********** Error uploading JATOS file, please enter it before any Demographic File **********\n')
        sys.exit(1)

def percent_calculation(df):
    """Calculates percent of data in the system flaged as Good
    df: given DataFrame
    Returns: 
        dataframe: updated with the new column 'Good_percent'
    """
    if "Above" in df.columns and "Below" in df.columns:
        df["Sum"] = df["Above"].fillna(0) + df["Below"].fillna(0) + df["Good"]
    elif "Above" in df.columns:
        df["Sum"] = df["Above"].fillna(0) + df["Good"]
        print("There are no responses below the minimum.")
    elif "Below" in df.columns:
        df["Sum"] = df["Below"].fillna(0) + df["Good"]
        print ("There are no responses Above the maximum.")
    else:
        df["Sum"] = df["Good"]
        print("There are no responses outside the norm.")
    df["Good_percent"] = df["Good"]/df["Sum"]
    return df


############ MAIN PART ############ 
############ JATOS DATA ############ 
args = sys.argv[1:]

print(f'\nUsed files : {args}\n')

if len(args) <= 1:
    print('********** Please provide all arguments: the first one is the JATOS and all the demographic CSV files.**********\n')
    sys.exit(1)

for file in args:
    if (os.path.splitext(file)[1] != '.txt' ) & (os.path.splitext(file)[1] != '.csv'):
        print(f'\n********** file "{file}" not found. Please make sure the file exists and try again.**********\n')
        sys.exit(1)

check_files(args)

df_jatos = upload_jatos(args[0])
df_jatos_participant_ids = df_jatos['participant_id'].unique()
df_jatos['group_id'] = df_jatos['group_id'].astype('str')
unique_identifiers = df_jatos['project_identifier'].dropna().unique()
print("Project name:", unique_identifiers)
print(f'You are processing {len(args)-1} demographic files\n')

############ DEMOGRAPHICS DATA ############
final_meta = pd.DataFrame()
for num in range(1, len(args)):
    provider_file = args[num]
    df_meta = pd.read_csv(provider_file, header=1, low_memory=True)

    # Load data from the demographics data (csv. file)
    if 'RespondentUrlCode' in df_meta.columns:
        print('Reading Cint file: ', provider_file)
        df_meta = df_meta[['RespondentUrlCode', 'Status', 'Gender', 'Age', 'TargetGroupName']].copy()
        df_meta.columns = ['participant_id', 'Status', 'Gender', 'Age', 'TargetGroupName']
        df_meta_status_5_ids = df_meta[df_meta['Status'] == 5]['participant_id']
        df_meta_5 = df_meta[df_meta['Status'] == 5].copy()
        df_meta_5['provider'] = 'ct'
        df_meta_5['demographic_file'] = provider_file
        final_meta = pd.concat([final_meta, df_meta_5], axis=0)

    else:
        df_meta = pd.read_csv(provider_file, low_memory=True)
        if 'Transaction ID' in df_meta.columns:
            print('Reading PM file: ', provider_file)
            df_meta_rename = {'Transaction ID' : 'participant_id', 'Respondent Status Code' : 'Status'}
            df_meta.rename(columns = df_meta_rename, inplace = True)
            df_meta = df_meta[['participant_id', 'Status', 'Age', 'Gender']].copy()
            df_meta['TargetGroupName'] = 'uknown'
            df_meta_status_21_ids = df_meta[df_meta['Status'] == 21]['participant_id']
            df_meta_21 = df_meta[df_meta['Status'] == 21].copy()
            df_meta_21['provider'] = 'pm'
            df_meta_21['demographic_file'] = provider_file
            final_meta = pd.concat([final_meta, df_meta_21], axis=0)

        else:
            print(f'WARNING: Uknown Provider in file {provider_file}, names of the columns in file do not match!')
            pass

for file in final_meta.demographic_file.unique():
    print(f'\nNumber of identified participants in the file {file}: ', final_meta[final_meta['demographic_file']==file]['participant_id'].nunique())
    print('')
print('\nTotal number of participants in provider files: ', final_meta.participant_id.nunique())
ghost_id = final_meta.loc[~final_meta['participant_id'].isin(df_jatos_participant_ids)][['participant_id','Age','Gender','TargetGroupName', 'demographic_file', 'provider']]
print('\nTotal number of ghost participants in provider files: ', ghost_id.participant_id.nunique())

df_merge = df_jatos.merge(final_meta, on="participant_id", how="inner")
print('\nTotal number of matching participants with jatos file: ', final_meta.participant_id.nunique())

df_merge= df_merge[df_merge['reason_to_end_the_behavioral_task_code']==13].copy()
print('\nTotal number of participants with behavioral task code 13: ', df_merge.participant_id.nunique())


IDs_per_group = tabulate_group(df_merge,["participant_id","group_id", "Gender", "Age","demographic_file", "provider"]).reset_index().sort_values(by="group_id")

df_merge = df_merge[(df_merge['trial_name']=="Association")&(df_merge['session_name']=="TSF")].copy()

df_merge["Flag"] = df_merge.apply(filter_conditions, axis=1)

tab = tabulate_group(df_merge,["participant_id","group_id","Flag"])

tab_pivot = pd.pivot(tab,values=0, index=["participant_id"], columns="Flag")
tab_pivot = percent_calculation(tab_pivot)

final_df = pd.merge(IDs_per_group,tab_pivot, on="participant_id")
final_df2 =final_df[final_df['Good_percent']>=0.5]

unique_participant_ids = final_df2['participant_id'].nunique()

bad_ids = final_df[~final_df['participant_id'].isin(final_df2["participant_id"].to_list())]

output_folder = 'QA_Outputs'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with pd.ExcelWriter(os.path.join(output_folder, 'QA_report_.xlsx')) as writer:

    tabulate_group(final_df2,["group_id"]).to_excel(writer, sheet_name="Count")
    final_df2[["participant_id","group_id","Good_percent", "Age", "Gender","demographic_file", "provider"]].to_excel(writer, sheet_name="Good IDs") 
    bad_ids[["participant_id","group_id","Good_percent", "Age", "Gender","demographic_file", "provider"]].to_excel(writer, sheet_name='Bad IDs')
    ghost_id.to_excel(writer, sheet_name="Ghost IDs")    
    gender_count = final_df2.groupby('Gender')['participant_id'].count().reset_index()
    gender_count.columns = ['Gender', 'Count']
    total_participants = gender_count['Count'].sum()
    gender_count['Percentage'] = (gender_count['Count'] / total_participants * 100).round(2)
    gender_stats = pd.concat([gender_count['Gender'], gender_count['Count'], gender_count['Percentage']], axis=1)
    gender_stats.to_excel(writer, sheet_name='Gender Stats', index=False)


# Print the count of common participant_ids
print('\nNumber of participants with low score on QA, below 50% good answers:', len(bad_ids['participant_id']))
print('\nNumber of participants who pass the QA with 50% or more good answers:', unique_participant_ids)

clean_df = pd.merge(final_df2, df_jatos, on=['participant_id', 'group_id'], how='inner')

# Produce raw jatos file
outfile_raw = 'RawJatos_' + str(unique_identifiers[0]) + '.csv'
df_jatos.to_csv(os.path.join(output_folder, outfile_raw), index=False)
clean_df.to_csv(os.path.join(output_folder, 'cleaned_df.csv'), index=False)

print('\nQA is completed\n')
