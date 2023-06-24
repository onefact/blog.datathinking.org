import pandas as pd

filename = 'C:/Users/SPECTRE/anaconda3/blog.datathinking.org/Blogpost_IRIS/final_file_PAT_Res.csv' 
error_lines = []

with open(filename, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()
        columns = line.split(',')
        num_values = len(columns)
        if num_values != 69:  # Adjust the expected number of columns accordingly
            error_lines.append((line_number, num_values))

print(f"Found {len(error_lines)} lines with inconsistent column count:")
for line_number, num_values in error_lines:
    print(f"Line {line_number}: {num_values} values")



