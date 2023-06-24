# Read the modified CSV file
with open('modified_file_PAT_Res.csv', 'r') as file:
    lines = file.readlines()

# Process the data and write to a new file
output_file = 'final_file_PAT_Res.csv'

with open(output_file, 'w') as file:
    for line in lines:
        # Remove quotation marks
        cleaned_line = line.replace('"', '')

        # Replace commas after "Patent application" with "-"
        cleaned_line = cleaned_line.replace('Patent applications,', 'Patent applications -')

        # Split the line on commas
        columns = cleaned_line.split(',')

        # Replace empty values with zeros
        for i in range(len(columns)):
            if columns[i] == '':
                columns[i] = '0'

        # Write the modified line to the file
        file.write(','.join(columns) + '\n')

print(f"Modified data has been written to '{output_file}'.")






