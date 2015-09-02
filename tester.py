def test(got, expected):
  if got == expected:
    prefix = 'Correct'
  else:
    prefix = 'Wrong'
  return '%s. Got: %s' % (prefix, repr(got))
