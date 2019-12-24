import re
from flask import Flask
import json

# print(Flask.__doc__)

# string = '4×185'

# print("===========")
# print(type(string))
# print(string[-1])
# print(type(string[-1]))
# print("===========")
# num1 = eval(string)
# print(num1)
# print(type(num1))
# print("===========")
# num2 = eval(string[-1])
# print(num2)
# print(type(num2))
# print("===========")
# print(string[:])


# string = '2887米'
# print(string[-1])
#
# if string[-1].encode('UTF-8').isalpha():
#     print('yes')
# else:
#     print('no')


# string = '计划去拆除上下界断路器3台面,去除上下界断路器3台面'
# pattern = r'计划.*?(拆除|去除).*?断路器'
# match = re.search(pattern, string)
# if match:
#     t = match.group()
#     print('yes')
#     print(t)
# else:
#     print('no')

# if True:
#     print('yes')
# else:
#     print('no')

try:
    list_test = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    json_test = json.dumps(list_test)
    print(json_test)
except:
    print('no')