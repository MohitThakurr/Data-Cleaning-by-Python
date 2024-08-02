import pandas as pd
import numpy as np
#Numpy Data Cleaning xyz
class DataCleaner:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        #Self.git update
    
    def handle_missing_values(self, strategy='mean', fill_value=None, columns=None):
        if columns is None:
            columns = self.data.columns
        
        for column in columns:
            if strategy == 'mean':
                self.data[column].fillna(self.data[column].mean(), inplace=True)
            elif strategy == 'median':
                self.data[column].fillna(self.data[column].median(), inplace=True)
            elif strategy == 'mode':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            elif strategy == 'constant':
                self.data[column].fillna(fill_value, inplace=True)
            else:
                raise ValueError("Invalid strategy: choose from 'mean', 'median', 'mode', 'constant'")
    #Duplicate removing from Main file- 383847
    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)
            self.data.drop_duplicates(inplace=True)

    def add_column(self, column_name, data):
        self.data[column_name] = data
         def add_column(self, column_name, data):
        self.data[column_name] = data
    
    def transform_column(self, column_name, function):
        self.data[column_name] = self.data[column_name].apply(function)
    
    def save_cleaned_data(self, output_file_path):
        self.data.to_csv(output_file_path, index=False)

    def get_data(self):
        return self.data
#SelfDataCourse 2223
#Concluded
