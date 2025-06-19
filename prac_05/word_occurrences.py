"""
Word Occurrences
Estimate: 1 hour
Actual:   30 minutes
"""

# Get user's text.
text = input("Text: ")

# Count words
word_count = {}

words = text.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word in sorted(word_count):
    width = 11
    print(f"{word:{width}}: {word_count[word]}")






