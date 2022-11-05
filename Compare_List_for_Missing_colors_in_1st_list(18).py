colorlist1=list(input("\nEnter the colors\n").split(" "))
colorlist2=list(input("\nEnter the colors\n").split(" "))
c=[]
c=[i for i in colorlist1 if i not in colorlist2]
print(c)