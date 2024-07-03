#fuction and modules 
# def print_numbers(*args):
#     for number in args:
#          print(number)

# print_numbers(1,2,3,4)

# def print_info(**kwargs):
#      for key,value in kwargs.items():
#          print(f"{key}:{value}")

# print_info(name="shree",age=20) #literal values


# # return value 
# def multiply(a,b):
#      return a*b
# result= multiply(4,5)
# print(result)


#without return value 

# def multiply(a,b):
#      result = multiply(4,5)
# print(result) #without return value

# #global and local variable

# x=10   #global variable
# def add():
#      x=20    #local variable
#      print(x)   

# def my_decorator(func):
#     def wrapper():
#         print("something is happening before the function")
#         func()
#         print("something is happening after the function")
#         return wrapper
# @my_decorator
# def say_hello():
#     print("hello")

# say_hello

#modules

# import sys
# print(sys.version)



#random number generator
# import random
# print(random.randint(1,10))

#regular expression 

# import re
# pattern = re.compiler(r,\)
                      


                      #csv

import csv

with open('data.csv',mode='w',newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name','age'])
    writer.writerow(['shree',20])
