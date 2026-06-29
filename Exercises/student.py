# Create a file: student_info.py
# Task:
#  Write a program that:
# 1. Asks for:Name Age Favorite number
# 2. Prints:
# Hello Ekene, you are 20 years old.
# In 5 years, you will be 25.
# Your favorite number doubled is 14.

print('Welcome UST student')

name = input('Enter your name here:\n ')

age = int(input('Enter your age:\n '))

number = int(input('What is your favourite number ?\n '))

print(f'Hello {name}, you are {age}years old!')

print(f'In 5 years, you will be {age + 5}')

print(f'Your favourite number doubled is, {number * 2}')

