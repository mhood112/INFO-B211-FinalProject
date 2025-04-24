import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"c:\Users\Simon\Documents\archive\Cleaned_Quality_of_Life.csv"
df = pd.read_csv(file_path)

# Convert relevant columns to numeric (if not already)
df['quality_of_life_value'] = pd.to_numeric(df['quality_of_life_value'], errors='coerce')

# Drop rows with missing values in the 'quality_of_life_value' column
df_cleaned = df.dropna(subset=['quality_of_life_value'])

# Ensure there are no duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Find the countries with the lowest and highest quality of life
df['quality_of_life_value'] = pd.to_numeric(df['quality_of_life_value'], errors='coerce')
df_cleaned = df.dropna(subset=['quality_of_life_value'])

lowest_quality = df_cleaned.loc[df_cleaned['quality_of_life_value'].idxmin()]
highest_quality = df_cleaned.loc[df_cleaned['quality_of_life_value'].idxmax()]

# Compare key factors
comparison = pd.DataFrame({
    'Lowest Quality of Life': lowest_quality,
    'Highest Quality of Life': highest_quality
})

print("Comparison of Lowest and Highest Quality of Life:")
print(comparison)