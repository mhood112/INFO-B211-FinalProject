import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"c:\Users\Simon\Documents\archive\Cleaned_Quality_of_Life.csv"
df = pd.read_csv(file_path)

# Convert relevant columns to numeric
df['purchasing_power_value'] = pd.to_numeric(df['purchasing_power_value'], errors='coerce')
df['cost_of_living_value'] = pd.to_numeric(df['cost_of_living_value'], errors='coerce')
df['quality_of_life_value'] = pd.to_numeric(df['quality_of_life_value'], errors='coerce')

# Drop rows with missing values in relevant columns
df_cleaned = df.dropna(subset=['purchasing_power_value', 'cost_of_living_value', 'quality_of_life_value'])

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['purchasing_power_value'], df_cleaned['cost_of_living_value'], c=df_cleaned['quality_of_life_value'], cmap='viridis', alpha=0.7)
plt.colorbar(label='Quality of Life Value')
plt.title("Purchasing Power vs Cost of Living (Colored by Quality of Life)")
plt.xlabel("Purchasing Power Value")
plt.ylabel("Cost of Living Value")
plt.show()