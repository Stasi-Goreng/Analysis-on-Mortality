import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Annual cause death numbers new.csv')

#print(data.head())

data_cols = list(data.columns)
strip_cols = [col.strip() for col in data_cols if col.endswith('\n\n\n\n\n\n')]
strip_cols = ['Entity', 'Code', 'Year'] + strip_cols + ['Acute hepatitis fatalities', 'Measles fatalities']
data.columns = strip_cols

#print(strip_cols)
data_entity = data.groupby('Entity')['Parkinson s fatalities'].sum()

data_entity_ger = data[data['Entity'] == 'Germany']
data_parkinson = data_entity_ger[['Year', 'Parkinson s fatalities', 'Dementia fatalities']]
print(data_parkinson.head())
parkinson_line = sns.lineplot(data=data_parkinson, x='Year', y='Parkinson s fatalities', label='Parkinson s fatalities', palette='pastel')
dementia_line = sns.lineplot(data=data_parkinson, x='Year', y='Dementia fatalities', label='Dementia fatalities', palette='pastel')
plt.legend(title='Fatalities', bbox_to_anchor=(1.05, 1), loc='upper right', borderpad=0)
plt.ylabel('Fatalities')
plt.show()

western_countries = data[data['Entity'] == 'England']
western_countries = pd.concat([data[data['Entity'] == 'Germany'], western_countries])
western_countries.reset_index(drop=True, inplace=True)
print(western_countries.head())
