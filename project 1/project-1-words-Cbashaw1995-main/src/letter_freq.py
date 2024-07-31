"""
CSAPX Project1: Words
Author: Connor Bashaw @ RIT CS

letter_freq.py, compute the frequency of each letter, a-z, across the total occurrences of all words over all years

Usage:
$ python3 letter_freq.py [--output #] [--plot] filename
"""
import argparse
import string
import sys
import matplotlib.pyplot as plotter


def parse_args() -> argparse.Namespace:
    """
    Parse the command line arguments using argparse
    :return: the parsed command line arguments
    """
    # Initialize arg parse to variable name
    parser = argparse.ArgumentParser()

    # Add command line arguments
    # File to look through
    parser.add_argument('filename',
                        type=str, help='a comma separated value uni-gram file')
    # Will initiate text output
    parser.add_argument('-o', '--output',
                        action='store_true', help='display letter frequencies to standard output')
    # Will initiate matplot graphing
    parser.add_argument('-p', '--plot',
                        action='store_true', help='plot letter frequencies using matplotlib')
    return parser.parse_args()


def letterCountDictMaker(file):
    """
    Takes a file as input and returns a dictionary that contains relative frequency by using occurrences of a letter
    frequency of character usage compared to total count of letters
    :param file: csv file to look for provided from user input in args
    :return:
    """
    # Make a dictionary containing keys as  all lower case letters and initializes all values to 0
    letterFreq = {char: 0 for char in string.ascii_lowercase}

    # Try and except loop found in file not found error python doc
    try:
        # Read file as we did in people.py
        with open(file) as file:
            # Iterate each line
            for line in file:
                # Split on comma and space. remove both from line
                keyParts = line.strip().split(', ')
                if len(keyParts) == 3:
                    # Each of 3 parts of the split are now labeled
                    word, year, count = keyParts

                    # Convert to lower case in case not already in lower
                    word = word.lower()
                    # For each character in the word the count is then incremented in frequency
                    for char in word:
                        if char in string.ascii_lowercase:
                            letterFreq[char] += int(count)
    # Throws error if args.filename is not present in data folder.
    except FileNotFoundError:
        print(f"Error: {file} does not exist!")
        sys.exit(1)

    return letterFreq


def calc_frequency(letter_counts):
    # Get total for all values within letter count dictionary
    total_count = sum(letter_counts.values())

    # Create a new dictionary with keys of all 26 lower case letters set to the value of the frequency (count of
    #  Letter) / (total Count)
    letter_count_dict = {char: count / total_count for char, count in letter_counts.items()}
    return letter_count_dict


def main():
    # Initializes arg parse
    args = parse_args()

    # Stores filename from arg parse
    file = args.filename

    # Makes dictionary of letter counts
    letter_counts = letterCountDictMaker(file)

    # Takes letter total count dictionary and uses the values within to create a total frequency dictionary
    letter_frequencies = calc_frequency(letter_counts)

    # Prints the letter frequencies to the standard output. if given -o or --output prompt
    if args.output:
        for char, freq in sorted(letter_frequencies.items()):
            print(f'{char}: {freq}')

    # Plots the bar plot for frequencies if given -p or --plot
    if args.plot:
        # Make list of all letters
        letters = list(string.ascii_lowercase)
        # For each character in the list of letters return the frequency of the given character
        frequencies = [letter_frequencies[char] for char in letters]

        plotter.figure(figsize=(10, 6))
        plotter.bar(letters, frequencies, width=1, color='purple', edgecolor='black')
        plotter.title(f'Letter Frequencies: {file}')
        plotter.xlabel('Letters')
        plotter.ylabel('Frequency')
        plotter.show()


if __name__ == '__main__':
    main()
