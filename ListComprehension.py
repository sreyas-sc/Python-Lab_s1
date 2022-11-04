a=list(map(int,input("Enter the list").split(" ")))
b=[x for x in a if x>0]
print("Positive integers generated from integer list\n")
print(b)

print("Square of N numbers\n")
a=list(map(int,input("Enter the list").split(" ")))
print(a)
b=[x*x for x in a]
print(b)

a=list(input("Enter the word\n"))
b=['a','e','i','o','u','A','E','I','O','U']
c=[x for x in a if x in b]
print("Vowel list in word",c)

a=list(input("Enter the word\n"))
b=[ord(x) for x in a]
print(b)

