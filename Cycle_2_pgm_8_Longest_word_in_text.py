def longest_Length(a):
    a=list((a).split(" "))
    length=len(a)
    temp_length=0
    for i in range(1,length):
        if(temp_length<len(a[i])):
            temp_length=len(a[i])
            val=a[i]
    print("The longest word is ",val,"with lenght",temp_length)

a=input("enter the text")
longest_Length(a)