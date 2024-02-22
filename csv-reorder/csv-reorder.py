import csv  # import CSV module for reading/writing CSV files
import urllib.request  # import urllib.request module for opening URLs
import os  # import os module for interacting with OS

# define transform_csv function with four parameters:
# input CSV file path/URL, headings of 1st and 2nd target columns, name of output CSV file (without file extension)


def transform_csv(input_file, first_column, second_column, output_file):
    if input_file.startswith('http://') or input_file.startswith('https://'):  # check if input is retrieved from URL
        with urllib.request.urlopen(input_file) as response:  # open input file from URL
            lines = response.read().decode('utf-8').splitlines()  # read, decode as UTF-8 (to convert bytes object into string), split string into lines (lines variable containing list of strings, 1 string per CSV row)
    else:
        with open(input_file, 'r', newline='', encoding='utf-8') as file:  # open input file (from current dir or via absolute/relative file path) in read mode, universal newlines mode disabled and text specified as UTF-8-encoded
            lines = file.readlines()  # read lines and store list of lines in lines variable

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
    output_file = output_file + '_transformed.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(rearranged_header)
        csv_writer.writerows(rearranged_data)

    return output_file

# Example usage:
input_file_path = 'https://raw.githubusercontent.com/auden-in-austria-digital/aad-data/main/doc-data/csv/img_id.csv'
first_column_heading = 'doc_id'
second_column_heading = 'img_id'
output_file = 'output-csv'

transformed_file = transform_csv(input_file_path, first_column_heading, second_column_heading, output_file)
print(f'Transformed CSV written to: {transformed_file}')