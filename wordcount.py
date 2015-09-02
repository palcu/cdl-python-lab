# Wordcount exercise

# The main() below is already defined and complete. It calls print_words()
# and print_top() functions which you write.

# 0. Implement read_contents(filename), that takes the file name and returns
# a list of words.

# 1. Implement the print_words(text) function that counts how often each
# word appears in the text and prints:
# word1 count1
# word2 count2
# ...

# Print the above list in order sorted by word (python will sort punctuation to
# come before letters -- that's fine). Store all the words as lowercase,
# so 'The' and 'the' count as the same word.

# 2. Implement the print_top(text) function which is mostly similar
# to print_words() but which prints just the top 20 most common words sorted
# so the most common word is first, then the next most common, and so on.

# Use str.split() (no arguments) to split on all whitespace.

# Workflow: don't build the whole program at once. Get it to an intermediate
# milestone and print your data structure.

# When that's working, try for the next milestone.


def read_contents(filename):
  return


def print_words(text):
  return


def print_top(text):
  return


# Do not touch
filename = "small.txt"
text = read_contents(filename)
print_words(text)
print_top(text)

