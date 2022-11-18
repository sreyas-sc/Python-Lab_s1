def sum_list():
    a=[]
    total=0

    n=int(input("Enter the number of elememnts in the list "))
    for i in range(0,n):
        a.append(int(input("Enter the value ")))
    for i in  a:
        total=total+i
    print(total)
sum_list()
