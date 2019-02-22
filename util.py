def tobool(value):
  valid = {
    'True': True,
    'False': False
  }
  return valid[value]

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def isinteger(value):
  try:
    int(value)
    return True
  except ValueError:
    return False