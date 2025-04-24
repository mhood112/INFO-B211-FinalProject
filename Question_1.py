import pandas as pd

# Load the dataset
file_path = r"c:\Users\Simon\Documents\archive\Cleaned_Quality_of_Life.csv"
df = pd.read_csv(file_path)

# Group countries by healthcare category
healthcare_categories = df.groupby('health_care_category')['country'].apply(list)

print("Countries by Healthcare Category:")
print(healthcare_categories)