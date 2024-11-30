# Write a Program to print "Hello, World!"
print("Hello, World!")

# Write a Program to Print Integer Number Entered by User
num = int(input("Number Entered by User: "))
print(num)

# Write a Program to Add Two Integer Numbers Entered by User
num1 = int(input("Enter first No.: "))
num2 = int(input("Enter Second No.: "))

sum_result = num1 + num2
print("Add of two number is:", sum_result)

# Write a program where the user is asked to enter two integers (divisor and dividend) and the quotient and the remainder of their division is computed.(Both divisor and dividend should be integers.)

divisor = int(input("Enter your divisor: "))
dividend = int(input("Enter your dividend: "))

remainder = dividend % divisor

quotient = dividend // divisor

print("Remainder is:", remainder)
print("Quotient is:", quotient)

# Write a Program to Find Size of int, float, double and char in your computer

import sys

# Sizes of various data types in bytes
int_size = sys.getsizeof(int())
float_size = sys.getsizeof(float())
char_size = sys.getsizeof('c')  # A single character in Python

# Print the sizes
print(f"Size of int: {int_size} bytes")
print(f"Size of float (equivalent to double in Python): {float_size} bytes")
print(f"Size of char: {char_size} bytes")


# Write a Program to Swap Two Numbers

first_number = int(input("first no. is: "))
second_number = int(input("Second no. is:"))

first_number, second_number = second_number, first_number
print(first_number)
print(second_number)


# Write a Program to Multiply two decimal Numbers entered by User

first_no = float(input("enter your first name: "))
second_no = float(input("enter your second name: "))

multiply = first_no * second_no
print("product is:", multiply)

