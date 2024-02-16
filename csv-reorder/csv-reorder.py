import csv
import urllib.request
import os

def transform_csv(input_file, first_column, second_column):
    # Check if the input file is a URL or local file path
    if input_file.startswith('http://') or input_file.startswith('https://'):
        with urllib.request.urlopen(input_file) as response:
            lines = response.read().decode('utf-8').splitlines()
    else:
        with open(input_file, 'r', newline='', encoding='utf-8') as file:
            lines = file.readlines()

    # Parse CSV data
    csv_reader = csv.reader(lines)
    header = next(csv_reader)
    data = list(csv_reader)

    # Find indices of the selected columns
    first_col_index = header.index(first_column)
    second_col_index = header.index(second_column)

    # Sort data by the selected columns
    sorted_data = sorted(data, key=lambda x: (x[first_col_index], x[second_col_index]))

    # Rearrange columns so that the first selected column is first in the output table
    rearranged_header = [first_column, second_column] + [col for col in header if col not in (first_column, second_column)]
    rearranged_data = [[row[first_col_index], row[second_col_index]] + [row[i] for i in range(len(row)) if i not in (first_col_index, second_col_index)] for row in sorted_data]

    # Write the transformed CSV to a new file
    output_file = os.path.splitext(os.path.basename(input_file))[0] + '_transformed.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(rearranged_header)
        csv_writer.writerows(rearranged_data)

    return output_file

# Example usage:
input_file_path = 'example.csv'
first_column_heading = 'Column1'
second_column_heading = 'Column2'

transformed_file = transform_csv(input_file_path, first_column_heading, second_column_heading)
print(f'Transformed CSV written to: {transformed_file}')