string1=input("Enter a sentence: ");
x=string1.replace(string1[2],'$');
x=x.replace('$',string1[0],1);
print(x);