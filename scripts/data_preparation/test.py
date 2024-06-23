import pandas as pd

# Define the file path for the cleaned data
cleaned_data_path = (
    "C:\\PhD\\Codes\\railway_simulation\\data\\processed\\linie_cleaned.csv"
)

# Load the cleaned data
cleaned_df = pd.read_csv(cleaned_data_path)

# Inspect the first few lines of the cleaned data
print("First few lines of the cleaned file:")
print(cleaned_df.head())

# Print the summary of the cleaned data
print("Summary of the cleaned file:")
print(cleaned_df.info())
