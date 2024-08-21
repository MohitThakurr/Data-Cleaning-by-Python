from data_cleaning import DataCleaner

# Initialize the DataCleaner with the sample data
cleaner = DataCleaner('../data/sample_data.csv')

# Handle missing values
cleaner.handle_missing_values(strategy='mean', columns=['age', 'salary'])
cleaner.handle_missing_values(strategy='constant', fill_value='Unknown', columns=['city'])

# Remove duplicates(code in code)
cleaner.remove_duplicates()

# Add a new column and work
cleaner.add_column('salary_in_k', cleaner.get_data()['salary'] / 1000)

# Save the cleaned data
cleaner.save_cleaned_data('../data/cleaned_data.csv')

# Display the cleaned data 2

print("Cleaned Data:\n", cleaner.get_data())
print("Cleaned Data:\n", cleaner.get_data())
