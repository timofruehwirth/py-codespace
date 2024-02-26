# py-codespace

## transform_csv

**transform_csv.py** contains the **transform_csv()** function which transforms any CSV file by
- reading the input CSV file (from relative/absolute file path or URL),
- moving the first column selected to the first column from left and arranging the table rows according to this column's values (alphanumerically increasing),
- moving the second column selected to the second column from left and arranging those table rows that share the same values in the first column according to this second column's values (alphanumerically increasing), and
- writing the output CSV file (into the script's home directory).

The function takes four arguments:
- `input_file` is the name and location of the input CSV file (relative/absolute file path or URL)
- `first_column` is the header of the first column selected
- `second_column` is the header of the second colum selected
- `output_filename` is the name of the output CSV file (without .csv extension)

Script written with the support of ChatGPT 3.5.