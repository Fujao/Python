import string
import random

number_of_strings = 10
length_of_string = 35
for x in range(number_of_strings):
  x = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
  print(x)