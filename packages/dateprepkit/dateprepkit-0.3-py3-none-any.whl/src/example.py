# Import DataPrepKit
from DataPrepKit.DataPrepKit import DataPrepKit
# Initialize DataPrepKit with a DataFrame
prep_kit = DataPrepKit()

# Read data from a CSV file
csv_data = prep_kit.read_data('student-dataset.csv', 'csv')

# Generate a data summary
summary = prep_kit.data_summary()
print("Data Summary:")
print(summary)

# Handle missing values by removing
cleaned_data = prep_kit.handle_missing_values(strategy='remove')
print("\nData after handling missing values (removed):")
print(cleaned_data)

# Encode categorical data
encoded_df = prep_kit.encode_categorical_data(categorical_columns=['Gender', 'City'])
print("\nEncoded DataFrame:")
print(encoded_df)