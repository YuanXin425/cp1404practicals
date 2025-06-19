"""
Word Occurrences
Estimate: 1 hour
Actual:   30 minutes
"""

# Get user's text.
text = input("Text: ")

# Create an empty dictionary to store word counts
word_count = {}

# Split the text into individual words based on white space
words = text.split()

# Loop through each word and count its occurrences
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Sort the words in ascending order and print each word with its count
for word in sorted(word_count):
    width = 11
    print(f"{word:{width}}: {word_count[word]}")






