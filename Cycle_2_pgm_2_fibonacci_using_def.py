def fibonacci():  
    n=int(input("enter number"))

    a=0;
    b=1;

    #print(a,'\n')
    #print(b,'\n')

    for i in range(n):
        c=a+b;
        a=b;
        b=c;
        print(c)
fibonacci()   
