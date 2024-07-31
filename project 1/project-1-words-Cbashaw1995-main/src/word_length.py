"""
CSAPX Project1: Words
Author: Connor Bashaw

word_length.py, compute the average word length over a range of years. These results can be plotted as a line chart.

Usage:
$ python3 word_length.py [--output #] [--plot] start end filename
"""
import argparse
import sys
import matplotlib.pyplot as plotter


def parse_args() -> argparse.Namespace:
    """
    Parse the command line arguments using argparse
    :return: the parsed command line arguments
    """
    # initialize arg parse to variable name
    parser = argparse.ArgumentParser()

    # Add command line arguments
    # year to start searching from
    parser.add_argument('start', type=int,
                        help='the starting year range')
    # year to end search on
    parser.add_argument('end', type=int,
                        help='the ending year range')
    # File to look through
    parser.add_argument('filename', type=str,
                        help='a comma separated value uni gram file')
    # will initiate text output
    parser.add_argument("-o", "--output", action="store_true",
                        help="display the top OUTPUT (#) ranked words by number of occurrences")
    # will initiate matplot graphing
    parser.add_argument("-p", "--plot", action="store_true",
                        help="plot the word rankings from top to bottom based on occurrences")
    return parser.parse_args()


def wordLengthDictMaker(file):
    # initialize empy dictionary for each year's data
    wordLength = {}

    # Try and except loop found in file not found error python doc
    try:
        # read file as we did in people.py
        with open(file) as file:
            # iterate each line
            for line in file:
                # split on comma and space. remove both from line
                keyParts = line.strip().split(', ')
                if len(keyParts) == 3:
                    word, year, count = keyParts
                    # convert all parts of line to variables that contain an int version
                    word = len(word)
                    year = int(year)
                    count = int(count)

                    # if year is not in word length that year will be initialized to total length 0 and word count of 0
                    if year not in wordLength:
                        wordLength[year] = {'totalLength': 0, 'wordCount': 0}

                    # updates the dictionary for each year tracking total word length and word count for that year
                    # these variables are then added and assigned to values for each word
                    wordLength[year]['totalLength'] += word * count
                    wordLength[year]['wordCount'] += count
    # Throws error if args.filename is not present in data folder.
    except FileNotFoundError:
        print(f"Error: {file} does not exist!")
        sys.exit(1)
    return wordLength


def main():
    # Initializes arg parse
    args = parse_args()
    # Stores start year  from arg parse
    startYear = args.start
    # Stores end year from arg parse
    endYear = args.end
    # Stores filename from arg parse
    file = args.filename

    # Checks to make sure start is greater than end or throws error from guidelines.
    if startYear > endYear:
        print("Error: start year must be less than or equal to end year!")
        sys.exit(1)

    # Creates dictionary to store word length
    wordLength = wordLengthDictMaker(file)

    # Calculates and prints average word length for each year within start year and end year
    if args.output:
        # Iterates each year from start to end
        for year in range(startYear, endYear + 1):
            # Check if year is in word length and value is greater than 0
            if year in wordLength and wordLength[year]['wordCount'] > 0:
                # If condition above met, then we will calculate average length for a given year  divide total word
                # Length for that year by total count of words in that year
                avgLength = wordLength[year]['totalLength'] / wordLength[year]['wordCount']
                print(f"{year}: {avgLength}")

    # Plots line for average word length over specified years
    if args.plot:
        years = []
        avgLengthList = []

        # Iterate through each year in range from start to end
        for year in range(startYear, endYear + 1):

            # Check if year is in word length and value is greater than 0
            if year in wordLength and wordLength[year]['wordCount'] > 0:
                # Calculates word length for a year and dives total of all words / total count of words
                average = wordLength[year]['totalLength'] / wordLength[year]['wordCount']

                # If current year has valid data and the average is calculated we add this to the years list and
                # Average length to length list
                years.append(year)
                avgLengthList.append(average)

        plotter.figure(figsize=(10, 6))
        plotter.plot(years, avgLengthList, marker='*', color='purple')
        plotter.title(f"Average word lengths from {startYear} to {endYear}:{file}")
        plotter.xlabel('Year')
        plotter.ylabel('Average word length')
        plotter.grid()
        plotter.show()


if __name__ == '__main__':
    main()
