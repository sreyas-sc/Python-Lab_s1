def ing(s):
    if s[-3::]=="ing":
        #res=s[:-3:]+"ly"
        res=s+"ly"
        return res
    else:
        s=s+"ing"
        return s
        print(res)
s=input("enter a word: ")
print(ing(s))
