def pyr(n):
    for i in range(1,n+1):
        f=" "
        for j in range(1,i+1):
            f=f+str(i*j)+' '
        print(f)
m=int(input("enter  the number: "))
pyr(m)