import math

def check(start,end):

    a =[]

    for i in range(start,end):

        if(even(i) == 0 and sq(i) == 0):

            a.append(i)

    print(a)



def even(temp):

    flag = 0

    while(temp > 0):

            if((temp%10) % 2 == 0):
                
                temp = temp // 10

            else:

                flag = 1

                temp = temp // 10

    return(flag)

def sq(temp):

    a = int(math.sqrt(temp))

    if(a**2 == temp):

        return 0
    
    else:

        return 1



a = int(input("Enter a starting range"))

b = int(input("Enter a ending range"))

print(check(a,b))