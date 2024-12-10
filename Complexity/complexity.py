# import time;

# start = time.time()
# for i in range(1, 101):
#     print(i)
    
# print(time.time() - start)


# ///////////////

n = 123457  # Example number
sum_of_digits = 0

# Loop through each digit
for digit in str(n):  
    print(n, digit)# Convert number to string to iterate
    sum_of_digits += int(digit)  # Convert back to integer and add to the sum

print("Sum of digits:", sum_of_digits)  # Output: 15
