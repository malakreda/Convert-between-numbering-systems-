#بلال محمد عمر       20230097
#حبيبه احمد رجب        20230633
#ملك رضا محمد اسماعيل        20230584
def binary_nums(num1, num2):
  """
  Adds two binary numbers
  Args:
    num1: FIRST NUM
    num2: SECOND NUM

  Returns:
    Sum of the two numbers
  """

  result = ""
  carry = 0
  for k in range(len(num1) - 1, -1, -1):
    sum = num1[k] + num2[k] + carry
    if sum == 0:
      carry = 0
      result += "0"
    elif sum == 1:
      carry = 0
      result += "1"
    elif sum == 2:
      carry = 1
      result += "0"
    else:
      carry = 1
      result += "1"

  if carry == 1:
    result += "1"

  return result[::-1]

def subinary_num(num1, num2):
  """
  Subtracts two binary numbers.

  Args:
    num1: first num
    num2: second num

  Returns:
    subtraction for num1 and num2
  """

  result = ""
  borrow = 0
  for i in range(len(num1) - 1, -1, -1):
    diff = num1[i] - num2[i] - borrow
    if diff < 0:
      diff += 2
      borrow = 1
    else:
      borrow = 0

    result += str(diff)

  return result[::-1]

def complement_firstnumber(number):
  """
  Calculates the first complement for a binary number

  Args:
    number: second num

  Returns:
    The first complement to the number
  """

  complement = ""
  for bit in number:
    complement += str(not int(bit))

  return complement

def complement_secondnumber(number):
  """
  Calculates the second complement of a binary number

  Args:
    number: second num

  Returns:
    The second complement to the number.
  """

