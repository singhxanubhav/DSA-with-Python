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
#     # print(fact)

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


#5 Write a Program to Display Fibonacci Series upto certain number n (n is entered by user) Example: n=100 Output: Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

    
limit = int(input("Enter a number: "))


a, b = 0, 1

print(a)
print(b)

c = a + b

while c < limit:
    
    print(c)
    a = b
    b = c
    c = a + b
        
