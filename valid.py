def get_integer(prompt):
  """
  Prompts the user an integer and returns a valid integer
  :param prompt: a string with the prompt for user
  :return: a valid integer
  """
  num = 0
  valid = False
  
  while not valid:
      try:
          num = int(input(prompt))
          valid = True
      except:
          print("Invalid integer.")

  return num


def get_float(prompt):
  """
  Prompts the user an float and returns a valid float
  :param prompt: a string with the prompt for user
  :return: a valid float
  """
  num = 0
  valid = False
  
  while not valid:
      try:
          num = float(input(prompt))
          valid = True
      except:
          print("Invalid float.")

  return num