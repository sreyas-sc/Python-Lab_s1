list=list(input("\nEnter the list elements(Numbers)\n").split(" "))
list2=[]
for x in list:
    if int(x)%2!=0:
        list2.append(x);

print(list2);