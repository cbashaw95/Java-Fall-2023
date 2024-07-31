"""
CSAPX Project1: Words
Author: Connor Bashaw @ RIT CS

word count.py, is able to count the total number of occurrences of a word across all year

Usage:
$ python3 word_count.py [--output #] [--plot] word filename
"""
import argparse
import sys


def parse_args() -> argparse.Namespace:
    """
    Parse the command line arguments using argparse
    :return: the parsed command line arguments
    """
    # Initialize arg parse to variable name
    parser = argparse.ArgumentParser()

    # Add command line arguments
    # Word to count usage of
    parser.add_argument("word", type=str,
                        help='a word to display the total occurrences of')
    # File to look through
    parser.add_argument("filename", type=str,
                        help='a comma separated value file')

    return parser.parse_args()


def wordCountDictMaker(file):
    """
    Takes in a file as input and returns a dictionary containing words
    :param file: csv file to look for provided from user input in args
    :return: word count dictionary that has a key of word and a value of total count
    """
    # Initialize empty dictionary
    wordCountDict = {}

    # Try / except found in file not found error python docs to throw error. https://docs.python.org/3/library/exceptions.html
    try:
        # Read file as we did in people.py excercise with class.
        with open(file) as file:
            # Iterate each line
            for line in file:
                # Split on comma and space. remove both from line
                keyParts = line.strip().split(', ')

                # If line does not have 3 parts if it does move forward and continue
                if len(keyParts) == 3:
                    # Label each of the split key parts according to position in line. (Example would be (Request
                    # 2008 199329)
                    word, year, count = keyParts

                    # This adds a word to a dictionary or effectivley updates an existing count for a given word at
                    # Each spot of we will retrieve the current count of the word we are looking for, which will be
                    # Initialized to a default 0. Convert count to int and add to default value
                    wordCountDict[word] = wordCountDict.get(word, 0) + int(count)

    # Throws error if args.filename is not present in data folder.
    except FileNotFoundError:
        print(f"Error: {file} does not exist!")
        sys.exit(1)

    return wordCountDict


def main():
    # Initialize and store parse args function
    args = parse_args()

    # Store word and file as variables, taken from args
    word = args.word
    file = args.filename

    # Calls function to read file and make dictionary
    wordCountDict = wordCountDictMaker(file)

    # Error for if argument word does not appear
    if word not in wordCountDict:
        print(f"Error: {word} does not appear in {file}")
        sys.exit(1)

    # If word does exist it retrieves total count as total and prints formatted with input word
    total = wordCountDict[word]
    print(f"{word}: {total}")


if __name__ == '__main__':
    main()
