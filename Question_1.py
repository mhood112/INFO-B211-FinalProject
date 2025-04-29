import pandas as pd
from scipy.stats import chi2_contingency

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

    # Statistical analysis: Proportion of countries in each healthcare category
    category_counts = data['health_care_category'].value_counts()
    print("\nProportion of countries in each healthcare category:")
    print(category_counts / category_counts.sum())

    # Example: Chi-square test for independence (if applicable)
    if 'quality_of_life_category' in data.columns:
        contingency_table = pd.crosstab(data['health_care_category'], data['quality_of_life_category'])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        print("\nChi-square Test for Independence:")
        print(f"Chi2 Statistic: {chi2:.2f}, P-value: {p:.4f}, Degrees of Freedom: {dof}")
else:
    print("Error: Required columns 'health_care_category' or 'country' are missing in the dataset.")