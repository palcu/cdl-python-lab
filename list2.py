from tester import test


# D. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  # +++your code here+++
  return


test(sort_last([(1, 3), (3, 2), (2, 1)]),
     [(2, 1), (3, 2), (1, 3)])
test(sort_last([(2, 3), (1, 2), (3, 1)]),
     [(3, 1), (1, 2), (2, 3)])
test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
     [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  return


test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
     ['aa', 'bb', 'cc', 'xx', 'zz'])
test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
     ['aa', 'bb', 'cc', 'xx', 'zz'])
test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
     ['aa', 'aa', 'aa', 'bb', 'bb'])
