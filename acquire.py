import pandas as pd
from scipy.stats import entropy
import numpy as np
import matplotlib.pyplot as plt


# reading the data using the pandas read_csv function
def read_data():
    '''This function reads the data that has been downloaded in .text format. In order for this function to work, user must download the data and save it 
    in the same directory from where they are running thier Jupyter Notebook. Also, this function reads another dataframe and later merges both dataframes
    and returns as one'''
    df = pd.read_csv('anonymized-curriculum-access.txt', sep = ' ', header = None)


    # renaming the columns
    df.columns = ['date', 'time', 'page', 'user_id', 'cohort_id', 'ip']

    # getting second dataframe with additional details
    cohort_details = pd.read_csv('cohorts.csv')


    # merging both dataframes together
    df = df.merge(cohort_details, on = 'cohort_id', how = 'left')


    return df