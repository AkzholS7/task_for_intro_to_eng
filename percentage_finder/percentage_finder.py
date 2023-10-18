import argparse
from typing import List


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Find percentage of words containing specific characters')
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='Path to the text file')
    parser.add_argument('-c', '--chars', type=str, required=True,
                        help='Characters to search for')
    return parser.parse_args()


def find_percentage(file_path: str, chars: str) -> float:
    """
    Calculate the percentage of words in a file that contain any of the specified characters.

    :param file_path: Path to the text file.
    :param chars: Characters to search for.
    :return: Percentage of words containing any of the specified characters.
    """
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return 0.0

    total_words = len(words)
    if total_words == 0:
        print("Error: The file is empty or doesn't contain any words.")
        return 0.0

    count = sum(1 for word in words if any(char in word for char in chars))
    return (count / total_words) * 100


def main():
    args = parse_args()
    percentage = find_percentage(args.file, args.chars)
    print(
        f"The percentage of words containing '{args.chars}' is: {percentage:.2f}%")


if __name__ == "__main__":
    main()