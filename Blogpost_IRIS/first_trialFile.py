import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/SPECTRE/anaconda3/blog.datathinking.org/Blogpost_IRIS/modified_file_PAT_Res.csv', delimiter=',', quotechar='"', quoting=3, skipinitialspace=True)

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Remove quotation marks from values
df = df.apply(lambda x: x.str.strip('"'))

# Fill empty values with 0
df = df.fillna(0)

# Display a sample of the data
print(df.head())


