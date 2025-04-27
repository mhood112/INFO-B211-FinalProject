import pandas as pd

# Load the CSV file
file_path = r"c:\Users\Simon\Documents\archive\Cleaned_Quality_of_Life.csv"
data = pd.read_csv(file_path)

# Group countries by healthcare category and assess their quality
if 'health_care_category' in data.columns and 'country' in data.columns:
    healthcare_analysis = data.groupby('health_care_category')['country'].apply(list)

    # Display the results
    print("Countries grouped by healthcare quality levels:")
    for category, countries in healthcare_analysis.items():
        print(f"\n{category} ({len(countries)} countries):")
        print(", ".join(countries))
else:
    print("Error: Required columns 'health_care_category' or 'country' are missing in the dataset.")