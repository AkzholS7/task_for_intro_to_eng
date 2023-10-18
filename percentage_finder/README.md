# Percentage Finder

This script calculates the percentage of words in a specified text file that contain any of the specified characters.

## Usage

1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository or download the script `percentage_finder.py`.
3. Run the script from the command line, providing the path to the text file and the characters to search for as arguments.

```bash
python percentage_finder.py --file path/to/text/file.txt --chars abc
```

## Arguments

- `--file` or `-f`: Path to the text file. (Required)
- `--chars` or `-c`: Characters to search for. (Required)

## Example

```bash
python percentage_finder.py --file sample.txt --chars ae
```

This will output the percentage of words in sample.txt that contain either 'a' or 'e'.

## Error Handling

The script provides error messages for the following cases:

- The specified file does not exist.
- The file is empty or does not contain any words.

## Output

The script will output the percentage of words containing the specified characters to the console, formatted to two decimal places.

```
The percentage of words containing 'ae' is: 25.00%
```
