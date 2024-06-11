import pandas as pd

# Load dataset
df = pd.read_csv('projects.csv')

  # Konversi ke tipe data numerik

#print(df)


output = 'output.xlsx'
df.to_excel(output, index=False)

