a = int(input())
output_list = []
odd_number = 1

##Find a is odd or even
if(a%2==0):
##    a is even then run a loop in a-1 times
    for i in range(a-1):
        output_list.append(odd_number)
        odd_number+=2
else:
##    a is even then run a loop in a times
    for i in range(a):
        output_list.append(odd_number)
        odd_number+=2
    
print(output_list)
