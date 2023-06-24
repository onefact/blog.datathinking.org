import pandas as pd
with open(r'PAT_Nres.csv', 'r') as infile, \
     open(r'PAT_Nres.csv', 'w') as outfile:
    data = infile.read()
    data = data.replace("\"", "")
    outfile.write(data)
# Read the modified file
df = pd.read_csv('PAT_Nres.csv')
# Print the table
print(df[43:50])

