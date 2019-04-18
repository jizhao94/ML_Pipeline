'''
Machine Learning Pipeline for Homework 2
'''

import pandas as pd

def discretize_col(data, column):
    '''
    To discretize the continuous variable into three discrete variables: 0, 1, and 2;
    the boundaries are the minimum value, the 25% quantile, the 75% quantile, and the maximum value.
    
    Inputs: data, pandas dataframe
            column, string
    '''
    
    data[column] = pd.cut(data[column], bins=[data[column].min(), data[column].quantile(0.25), data[column].quantile(0.75),
                                              data[column].max()], labels=[0,1,2], include_lowest=True)


def to_binary(item):
    '''
    Convert the zipcode to the binary variable 0 or 1,
    in which 0 indicates that it is not in the South Side of the City of Chicago,
    while 1 indicates that it is in the South Side of the City of Chicago,
    concerning the fact that in this dataset, '60629' and '60637' are the only zipcodes of the South Side
    '''
    
    if item in ['60629','60637']:
        value = 1
    else:
        value = 0
    return value