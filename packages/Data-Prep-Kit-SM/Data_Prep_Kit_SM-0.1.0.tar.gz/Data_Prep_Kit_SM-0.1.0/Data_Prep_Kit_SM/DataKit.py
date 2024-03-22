
import numpy as np
import pandas as pd

class DataPrepKit:
    def __init__(self):
        pass
    
    def datareading(self, file_path):
       #to extract the file extention to seprate the file path from the extention
        file_extension = file_path.split('.')[-1] 
        if file_extension == 'csv':
            df = pd.read_csv(file_path)
        elif file_extension == 'json':
            df = pd.read_json(file_path)
        elif file_extension == 'xlsx':
            df = pd.read_excel(file_path)
        else:
            print('This type of file cannot be read')
            return None
        return df
    
    def data_stat(self, data):
     #to describe and give the stat of the data 
        summary = data.describe()
        return summary
    
    def data_mean(self, data):
    #get the average
        averages = data.mean()
        return averages
    
    def data_freq(self, data):
        most_frequent = data.mode().iloc[0]
        return most_frequent
    def handle_missing_values(self,df, strategy='drop', threshold=0.5, impute_value=None):
        #take a copy from the data 
        df_cleaned = df.copy() 
    
        if strategy == 'drop':
            df_cleaned.dropna(inplace=True)  # Drop rows with any missing values
        elif strategy == 'impute':
            df_cleaned.fillna(impute_value, inplace=True)  # Impute missing values with specified value
        elif strategy == 'threshold':
            missing_counts = df_cleaned.isnull().sum()  # Count missing values in each column
            columns_to_drop = missing_counts[missing_counts / len(df_cleaned) > threshold].index
            df_cleaned.drop(columns_to_drop, axis=1, inplace=True)  # Drop columns exceeding the threshold

        return df_cleaned
    def auto_one_hot_encode(df):

    # Identify categorical columns
        cat_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    # Perform one-hot encoding
        df_encoded = pd.get_dummies(df, columns=cat_columns)
    
        return df_encoded


