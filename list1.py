from tester import test


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # +++your code here+++
  return


test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # +++your code here+++
  return


test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
     ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
     ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
     ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# C. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  return


test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
test(remove_adjacent([]), [])
