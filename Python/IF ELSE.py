# # Write a Program to Check Whether Number is Even or Odd

# number = int(input("Enter your number: "))

# if(number%2 == 0):
    
#     print("Number is Even")

# else:
#     print("Number is Odd")


# # Write a Program to Check Whether a Character is Vowel or Consonant.

# char = input("Enter a single character: ").lower()

# if len(char) == 1 and char.isalpha():
   
#     if char in 'aeiou':
#         print(f"The character '{char}' is a vowel.")
#     else:
#         print(f"The character '{char}' is a consonant.")
# else:
#     print("Invalid input! Please enter a single alphabetic character.")


# # Write a Program to Find Largest Number Among Three Numbers entered by users

# num1 = int(input("Enter your first no: "))
# num2 = int(input("Enter your second no: "))
# num3 = int(input("Enter your third no: "))

# if num1>num2 and num1>num3:
#     print("num1 is largest")
    
# elif num2>num1 and num2>num3:
#     print("num2 is largest")
    
# else:
#     print("num3 is largest")
    
    
# # or
# largest = max(num1, num2, num3)
# print(f"The largest number is: {largest}")


# Write a Program which accepts coefficients of a quadratic equation from the user and displays the roots (both real and complex roots depending upon the discriminant).

import math

# Accept coefficients from the user
a = float(input("Enter the coefficient a (non-zero): "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Ensure 'a' is non-zero for a valid quadratic equation
if a == 0:
    print("This is not a quadratic equation. 'a' must be non-zero.")
else:
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Determine the nature of roots based on the discriminant
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The equation has two distinct real roots: {root1} and {root2}")
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        print(f"The equation has one repeated real root: {root}")
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The equation has complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
