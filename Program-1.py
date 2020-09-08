##Get the input from user
a = int(input())
b = int(input())

##Get the type of operation from user
type_of_operation = input("enter any of these for operation +,-,*,/")

##Doing Operations
if type_of_operation == "+":
    result = a+b
elif type_of_operation == "-":
    result = a-b
elif type_of_operation == "*":
    result = a*b
elif type_of_operation == "/":
    result = a/b
else:
    print("Invalid Operation")

##Final result
print(a,type_of_operation,b,": ",result)
