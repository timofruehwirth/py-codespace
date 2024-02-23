import csv  # import CSV module for reading/writing CSV files
import urllib.request  # import urllib.request module for opening URLs


# define transform_csv function
def transform_csv(input_file, first_column, second_column, output_filename):  # define function with parameters
    if input_file.startswith('http://') or input_file.startswith('https://'):  # check if input is retrieved from URL
        with urllib.request.urlopen(input_file) as response:  # open input file from URL
            lines = response.read().decode('utf-8').splitlines()  # read, decode as UTF-8 (to convert bytes object into string), split string into lines (lines variable containing list of strings, 1 string per CSV row)
    else:
        with open(input_file, 'r', newline='', encoding='utf-8') as file:  # open input file (from current dir or via absolute/relative file path) in read mode, universal newlines mode disabled and text specified as UTF-8-encoded
            lines = file.readlines()  # read lines and store list of lines in lines variable

    # parse CSV input data
    csv_reader = csv.reader(lines)  # pass lines variable to CSV reader object able to iterate over, and parse into list of fields, CSV rows
    header = next(csv_reader)  # return first (header) row to header variable as list of fields, advance to next row
    data = list(csv_reader)  # return remaining rows to data variable as list of lists, one list per row

    # find indices of selected columns
    first_column_index = header.index(first_column)  # find index of header of 1st selected column in header list
    second_column_index = header.index(second_column)  # find index of header of 2nd selected column

    # sort rows by selected columns
    sorted_data = sorted(data, key=lambda x: (x[first_column_index], x[second_column_index]))  # sort lists (of fields of rows) within data list based on tuples of values in selected columns of each row

    # rearrange columns in rows with selected columns at beginning
    new_header = [first_column, second_column] + [col for col in header if col not in (first_column, second_column)]  # create new list of headers, starting with headers of selected columns and iterating over remaining values of header list (through list comprehension)
    new_data = [[row[first_column_index], row[second_column_index]] + [row[i] for i in range(len(row)) if i not in (first_column_index, second_column_index)] for row in sorted_data]  # create new list of lists (i.e., rows), starting each list with values at indexes of selected columns and iterating over values at remaining indexes (through list comprehension)

    # write output CSV file
    output_file = output_filename + '.csv'  # construct full output file name from argument and file extension
    with open(output_file, 'w', newline='', encoding='utf-8') as file:  # create/open output CSV in write mode
        csv_writer = csv.writer(file)  # pass output file to CSV writer object
        csv_writer.writerow(new_header)  # write row from new list of headers
        csv_writer.writerows(new_data)  # write rows from new list of rows

    # print feedback
    print(f'Transformed CSV written to {output_file}.')

    # return output CSV file name for further use
    return output_file


# Example usage:
input_file_path = 'https://raw.githubusercontent.com/auden-in-austria-digital/aad-data/main/doc-data/csv/img_id.csv'
first_column_heading = 'doc_id'
second_column_heading = 'img_id'
output_filename = 'output-csv'

transform_csv(input_file_path, first_column_heading, second_column_heading, output_filename)
