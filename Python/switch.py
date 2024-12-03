# def check(choice):
#     match choice:
#         case 1:  
#             return "Monday"
#         case 2:
#             return "tuesday"
#         case 3:
#             return "wednesday"
#         case 4:
#             return "thursday"
#         case 5:
#             return "friday"
#         case 6:
#             return "saturday"
#         case _:
#             return "Invalid day"
        
        
# print(check(1))              
# print(check(8))       
# print(check(4))  

#  Write a Program to Make a Simple Calculator to Add, Subtract, Multiply or Divide Using Switch case
choice = int(input("Enter choice (1/2/3/4): "))

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        print(a / b)
            
        