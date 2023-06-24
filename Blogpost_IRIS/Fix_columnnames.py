import pandas as pd
from tabulate import tabulate

# Load the final file
df = pd.read_csv('final_file.csv')

# Add a new index column
#df['New Index'] = range(1, len(df) + 1)

# Specify the range of rows and columns you want to display
#subset = df.iloc[:10, :5]

# Convert the subset to a formatted table
#table = tabulate(subset, headers='keys', tablefmt='psql')

# Original column names
column_names = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
       '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

# Renamed column names
renamed_column_names = column_names[:-1]  # Exclude the last column

# Rename columns
for i in range(len(renamed_column_names)-1):
    df.rename(columns= )
    column_names[i] = renamed_column_names[i+1]

df.columns=column_names
print(column_names)

# Print the table
print(df.columns)
