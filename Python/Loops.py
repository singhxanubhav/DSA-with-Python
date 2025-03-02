# #1 Write a Program to Calculate Sum of first N Natural Numbers (here value of N is Entered by user)

# num = int(input("Give the Number: "))

# sum = 0
# for i in range(1, num+1):
#     sum = sum + i
#     print(sum)
    


  
#2 Write a Program to Generate Multiplication Table of a number (entered by the user) using a for loop.

# num = int(input("Give me a number: "))

# for i in range(1, 11):
#     mul = num * i
#     print(num, "*", i, "=", mul)
# print(mul)




# #3 Write a Program to Find Factorial of a given number N (N is entered by user)

# N = int(input("Give me a number(N): "))

# fact = 1
# for i in range(1, N + 1):
#     fact = fact * i
#     print(fact)

# print(fact)




#4 Write a Program to Display Fibonacci Series upto nth term (n is entered by user)

# Program to display Fibonacci series up to n-th term

# # Input: Get the number of terms from the user
# n = int(input("Enter the number of terms (n): "))

# a, b = 0, 1

# print(a)
# print(b)

# for i in range(2, n):
    
#     c = a + b
#     a = b
#     b = c
#     print(c)




# #5 Write a Program to Display Fibonacci Series upto certain number n (n is entered by user) Example: n=100 Output: Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

    
# limit = int(input("Enter a number: "))


# a, b = 0, 1

# print(a)
# print(b)

# c = a + b

# while c < limit:
    
#     print(c)
#     a = b
#     b = c
#     c = a + b





# #6 Write a Program to Find GCD or HCF of two numbers entered by user

# # Input two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Determine the smaller number
# smaller = min(num1, num2)

# # Initialize HCF
# hcf = 1

# # Loop through 1 to smaller
# for i in range(1, smaller + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i  # Update HCF
#     print(hcf)
    
# # Print the result
# print(f"The HCF of {num1} and {num2} is: {hcf}")


# or
# Input two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Determine the smaller number
# smaller = min(num1, num2)

# # Initialize variables
# hcf = 1
# i = 1

# # Use a while loop to find HCF
# while i <= smaller:
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i  # Update HCF if both numbers are divisible by i
#     i += 1  # Increment the counter

# # Print the result
# print(f"The HCF of {num1} and {num2} is: {hcf}")

 
 
 
# #7 Write a Program to Find LCM of two numbers entered by user

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# greater = max(num1, num2)


# for i in range(greater, (num1*num2) + 1):
#     if i%num1==0 and i%num2==0:
#         lcm = i
#         break

# print(lcm)
 
 
 
        
# #8 Write a Program to Reverse a given Number N by user


# # Input a number from the user
# number = int(input("Enter a number: "))

# # Initialize a variable to store the reversed number
# reversed_number = 0

# # Reverse the number using a while loop
# while number != 0:
#     digit = number % 10  # Get the last digit
#     reversed_number = reversed_number * 10 + digit  # Add it to the reversed number
#     number //= 10  # Remove the last digit from the number

# # Output the reversed number
# print(f"The reverse {reversed_number}")




# #9 Write a Program to display sum of all digits of a given Number N by user

# number = int(input("Enter a number: "))

# sum = 0

# while number != 0:
#     digit = number % 10
    
#     sum = sum + digit
#     number = number // 10
    
# print("Sum of digit is:", sum)    
    


# #10 Write a Program to Check Whether a Number is Prime or Not

# num = int(input("Enter a number(N): "))


# if num == 1:
#     print("it is not a prime")
# if num > 1:
      
#     for i in range(2, num):
#         if num % i == 0:
#             print("it is not a prime")
#             break
        
#     else:
#         print("it is a prime no.")
       
       
       

# #11  Write a Program to Display Prime Numbers Between Two Intervals (entered by user) Example: Enter two numbers: 0 20 Prime numbers between 0 and 20 are: 2 3 5 7 11 13 17 19

# num1 = int(input("enter a first no1: "))
# num2 = int(input("enter a second no2: ")) 


# for num in range(num1, num2+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
        
#         else:
#             print(num)        
            
          
    

  
      



