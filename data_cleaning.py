import pandas as pd
import numpy as np

# Load the CSV file
file_path = "/Users/miahood/Desktop/Final Project/Quality_of_Life.csv"
df = pd.read_csv(file_path)

# Tidy up column names: replace spaces with underscores and convert to lowercase
df.columns = df.columns.str.replace(' ', '_').str.lower()

# Remove all single quotes from the data
df.replace(to_replace=r"'", value='', regex=True, inplace=True)

# Strip whitespace and ensure all columns are properly typed
for col in df.columns:
    df[col] = df[col].astype(str).str.strip()  # Remove leading/trailing spaces
    try:
        df[col] = pd.to_numeric(df[col])  # Convert columns to numeric where possible
    except ValueError:
        pass  # Ignore columns that cannot be converted

# Replace all representations of 0 with NaN
df.replace(['0', 0, 0.0], np.nan, inplace=True)

# Remove ':' from the 'quality_of_life_value' column
if 'quality_of_life_value' in df.columns:
    df['quality_of_life_value'] = df['quality_of_life_value'].replace(to_replace=r':', value='', regex=True)
    df['quality_of_life_value'] = pd.to_numeric(df['quality_of_life_value'], errors='coerce')  # Ensure numeric

# Ensure 'property_price_to_income_value' is numeric and replace 0 with NaN
if 'property_price_to_income_value' in df.columns:
    df['property_price_to_income_value'] = pd.to_numeric(df['property_price_to_income_value'], errors='coerce')
    df['property_price_to_income_value'] = df['property_price_to_income_value'].replace(0, np.nan)  # Avoid inplace

# Standardize category naming
category_columns = [col for col in df.columns if 'category' in col]
for col in category_columns:
    df[col] = df[col].str.strip().str.lower().str.title()  # Standardize to "Title Case"

# Save the cleaned data to a new CSV file
cleaned_file_path = "/Users/miahood/Desktop/Final Project/Cleaned_Quality_of_Life.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")