import pandas as pd

df = pd.read_csv('cleaned_blood_type_distribution_by_country.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df['Country/Dependency'])
print(df[df['Country/Dependency'] == 'Russia'])
df['A-'] = pd.to_numeric(df['A-'], errors='coerce')
print(df[df['A-'] > 0.02])