# module used to acquire, clean, and prepare data

#libraries
import pandas as pd
import numpy as np

############## | acquire
def acquire(train_file, test_file):
    '''
    This function takes in train and test csv file names and writes the csv files to
    pandas Dataframes.
    '''
    
    train = pd.read_csv(train_file)
    print('Train file successfully written to train DataFrame.')
    
    test = pd.read_csv(test_file)
    print('Test file successfully written to train DataFrame.')
    
    return train, test