import csv

# Read the CSV file
with open('C:/Users/SPECTRE/anaconda3/blog.datathinking.org/Blogpost_IRIS/SUIC.csv', 'r') as file:
    reader = csv.reader(file)
    lines = list(reader)

# Remove extra values from each line
for i in range(len(lines)):
    if len(lines[i]) > 67:
        lines[i] = lines[i][:67]

# Write the modified lines back to a new CSV file
with open('modified_file_SUIC.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lines)

