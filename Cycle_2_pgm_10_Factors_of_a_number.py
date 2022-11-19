num = int(input("enter a number"))
print("\n Factors of", num)
i = 1
while i<=num:
    if num%i==0:
        print(i)
    i = i+1