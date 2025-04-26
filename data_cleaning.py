import pandas as pd
import numpy as np

# Load the CSV file
file_path = "/Users/miahood/Desktop/Final Project/Quality_of_Life.csv"
df = pd.read_csv(file_path)

# Normalize column names: replace spaces with underscores and convert to lowercase
df.columns = df.columns.str.replace(' ', '_').str.lower()

# Remove single quotes from all values in the DataFrame
df.replace(to_replace=r"'", value='', regex=True, inplace=True)

# Replace all 0 values with NaN
df.replace(0, np.nan, inplace=True)

# Remove ':' from the beginning of floats in the 'quality_of_life_value' column
if 'quality_of_life_value' in df.columns:
    df['quality_of_life_value'] = df['quality_of_life_value'].replace(to_replace=r'^:\s*', value='', regex=True)
    df['quality_of_life_value'] = pd.to_numeric(df['quality_of_life_value'], errors='coerce')  # Ensure numeric

# Drop rows where 'quality_of_life_category' is NaN
if 'quality_of_life_category' in df.columns:
    df = df[df['quality_of_life_category'].notna()]

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = "/Users/miahood/Desktop/Final Project/Cleaned_Quality_of_Life.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")