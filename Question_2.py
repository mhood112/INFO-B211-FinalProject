import pandas as pd
import seaborn as sns
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

# Correlation analysis
correlation = df_cleaned[['purchasing_power_value', 'cost_of_living_value', 'quality_of_life_value']].corr()
print("Correlation Matrix:")
print(correlation)

# Scatter plot
sns.scatterplot(data=df_cleaned, x='purchasing_power_value', y='cost_of_living_value', hue='quality_of_life_value', palette='viridis')
plt.title("Purchasing Power vs Cost of Living (Impact on Quality of Life)")
plt.xlabel("Purchasing Power Value")
plt.ylabel("Cost of Living Value")
plt.show()