def test(got, expected):
  if got == expected:
    return 'Correct'
  else:
    return 'Wrong. Got ' + repr(got)
