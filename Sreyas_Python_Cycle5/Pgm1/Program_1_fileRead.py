try:
    f1=open("test.txt","r")	
    a = [x.rstrip() for x in f1]
    print(a)
    f1.close()
except FileNotFoundError:  
    print("FileNotFound exception occured ")
except EOFError:
    print(EOFError)
except IOError:
    print("file not found IOError")
else:
    print("\n file operation done successully")
