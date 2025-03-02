num = int(input("Enter a number(N): "))


if num == 1:
    print("it is not a prime")
if num > 1:
      
    for i in range(2, num):
        if num % i == 0:
            print("it is not a prime")
            break
        
    else:
        print("it is a prime no.")
    