import pandas as pd
from scipy.stats import entropy
import numpy as np
import matplotlib.pyplot as plt



def prep_data(df):
    '''This function takes in the dataframe prepares it so that its ready for exploration. This function takes in a dataframe and returns 4 dataframes.
    One for Data Science students, one for Web Dev students, one for Staff, and one with nulls for cohort id'''

    # lets create a new columns with date and time together 
    df['date_time'] = df.date + ' ' + df.time

    # lets convert the new column we had just created to the datetime datatype
    df.date_time = pd.to_datetime(df.date_time)

    # lets put date_time as the index of our dataframe
    df = df.set_index('date_time')

    # splits the page viewd into 4 different columns to get better understanding of the lessons accessed
    df = pd.concat([df, df.page.str.split('/', 3, expand = True)], axis = 1)

    # we will rename the columns in following order
        # 0 = subdirectory
        # 1 = subdir1 and follows subdirectory
        # 2 = subdir2 and follows subdir1
        # 3 = subdir3 and follows subdir2
    df.rename(columns= {0:'subdir', 1: 'subdir1', 2: 'subdir2', 3:'subdir3'}, inplace = True)

    # data science df is the one where the program id is 3
    ds_df = df[df.program_id == 3]   

    
    # creating a separate dataframe that holds only the observations where the cohort id is null
    null_df = df[df.cohort_id.isnull()]

    # creating a separate dataframe that holds staff activities
    staff_df = df[df.name == 'Staff']

    # creating a dataframe that only holds the web development students
    web_dev = df[(~df.cohort_id.isnull()) & (df.name != 'Staff')]



    return ds_df, web_dev, staff_df, null_df
 




