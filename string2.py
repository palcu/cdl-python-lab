from tester import test


# E. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  return


test(verbing('hail'), 'hailing')
test(verbing('swiming'), 'swimingly')
test(verbing('do'), 'do')


# F. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  return


test(not_bad('This movie is not so bad'), 'This movie is good')
test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
test(not_bad('This tea is not hot'), 'This tea is not hot')
test(not_bad("It's bad yet not"), "It's bad yet not")


# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  return


test(front_back('abcd', 'xy'), 'abxcdy')
test(front_back('abcde', 'xyz'), 'abcxydez')
test(front_back('Kitten', 'Donut'), 'KitDontenut')
