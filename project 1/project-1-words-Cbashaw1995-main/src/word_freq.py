"""
CSAPX Project1: Words
Author: Connor Bashaw

word_freq.py, compute the popularity of a word in terms of the number of occurrences of all words over all years. The
relationship of the words, by rank, can be plotted as a log-log chart to reveal Zipf’s law.

Usage:
$ python3 word_freq.py [--output #] [--plot] word filename
"""
import argparse
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
    # Word to count usage of
    parser.add_argument('word',
                        help='a word to display the overall ranking of')
    # File to look through
    parser.add_argument('filename',
                        help='a comma separated value uni-gram file')
    # Will initiate text output
    parser.add_argument("-o", "--output", type=int, default=None,
                        help="display the top OUTPUT (#) ranked words by number of occurrences")
    # Will initiate matplot graphing
    parser.add_argument("-p", "--plot", action="store_true",
                        help="plot the word rankings from top to bottom based on occurrences")
    return parser.parse_args()


def wordFreqDictMaker(file):
    # Initialize empty dictionary and a total count variable to increment
    wordFreqDict = {}
    totalCount = 0

    # Try and except loop found in file not found error python doc
    try:
        # Read file as we did in people.py
        with open(file) as file:

            # Iterate each line
            for line in file:
                # Split on comma and space. remove both from line
                keyParts = line.strip().split(', ')
                if len(keyParts) == 3:
                    word, year, count = keyParts
                    count = int(count)
                    # Update word freq dictionary with word as key and count as value
                    wordFreqDict[word] = wordFreqDict.get(word, 0) + count
                    # Updates total count each time
                    totalCount += count
    # Throws error if args.filename is not present in data folder.
    except FileNotFoundError:
        print(f"Error: {file} does not exist!")
        sys.exit(1)

    return wordFreqDict


def main():
    # Read command line arguments.
    args = parse_args()
    # Stores word from arg parse
    word = args.word
    # Stores filename from arg parse
    file = args.filename

    # Creates a dictionary to store word frequency from a file
    wordFreqDict = wordFreqDictMaker(file)

    # If word is not in word dictionary throw an error
    if word not in wordFreqDict:
        print(f"Error: {word} does not appear in {file}")
        sys.exit(1)

    # Taken directly from class royale slides in recitation page 15 https://www.cs.rit.edu/~csapx/Recitations/03/03-SearchSortListFiles.pdf
    # Takes key (words) and sorts by values ( frequencies) reverse = true goes from highest to lowest
    # Lambda uses word as w and returns frequency from dictionary
    # WordSorted becomes a list of words sorted by frequency
    wordsSorted = sorted(wordFreqDict.keys(), key=lambda w: wordFreqDict[w], reverse=True)

    # Calculates ranking of a certain word using index + 1
    ranking = wordsSorted.index(word) + 1
    print(f"{word} is ranked #{ranking}")

    # Calculates rankings of specified word in list by frequency
    if args.output:
        # Creates range min and max
        numberOfWords = min(args.output, len(wordsSorted))
        # Iterates from min to max printing words and given frequencies
        for x in range(numberOfWords):
            w = wordsSorted[x]
            print(f"#{x + 1}: {w} -> {wordFreqDict[w]}")

    if args.plot:
        # Google saved my life here because I do not get matplot like I did turtle...
        # Sets rank from 1 to end of the list of words
        ranks = list(range(1, len(wordsSorted) + 1))
        # For each word in list of sorted words get the frequency
        counts = [wordFreqDict[word] for word in wordsSorted]

        plotter.figure(figsize=(10, 6))
        plotter.loglog(ranks, counts, marker='*', color='purple', label='word')

        plotter.annotate(text=word,xy=(ranking,counts[ranking] -1), xycoords='data', xytext=(10,10), textcoords='offset points',arrowprops=dict(facecolor='black', shrink=0.05))

        plotter.title(f"Word Frequencies: {file}")
        plotter.xlabel(f"Rank of word ('{word}' is rank {ranking})")
        plotter.ylabel("Number of occurrences")
        plotter.legend()
        plotter.grid()
        plotter.show()


if __name__ == '__main__':
    main()
