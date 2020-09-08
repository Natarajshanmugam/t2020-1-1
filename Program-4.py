##Get the input as integer list
input_list = list(map(int,input().split()))
##Initialize the empty dictionary
output_dict = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
total_count = 0
for key,value in output_dict.items():
    print(key,value)
    for i in input_list:
        if(i!=0 and i%key==0):
            total_count+=1
    output_dict[key]=total_count
    total_count=0
print(output_dict)
