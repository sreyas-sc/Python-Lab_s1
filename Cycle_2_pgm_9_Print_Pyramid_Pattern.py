def pyramid(rows):
    for i in range(0, rows):  
        for j in range(0, i + 1):  
            print("*", end=' ')  
        print(" ")  
    for i in range(rows , 0, -1):  
        for j in range(0, i - 1):  
            print("*", end=' ')  
        print(" ")  
n=int(input("enter a number"))
pyramid(n)