len1=int(input("enter the length of the first list: "))
len2=int(input("enter the length of the 2nd list:"))
l1=[]
l2=[]


for i in range(1,len1+1):
    l1.append(input("enter the "+str(i)+"element of the list : "))

for j in range(1,len2+1):
    l2.append(input("enter the "+str(j)+"element of the 2nd list"))

if len1==len2:
    print("Both list of same length")
else:
    print("They are not of the same length")
l1.sort()
l2.sort()
if l1==l2:
    print("the list are identical")
else:
    print("they are not identical")
a,b=set(l1),set(l2)
if(a&b):
    print("There are common elements")
else:
    print("No common member between them")
    
