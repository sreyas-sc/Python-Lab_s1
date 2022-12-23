class  rectangle:
    def __init__(self):
        self.__length=int(input("enter the length of the recangle: "))
        self.__width=int(input("enter the width of the rectangle: "))
        self.area=2*self.__length+self.__width;
    def __lt__(self,other):
        if(self.area<other.area):
            return True
        else:   
            return False
obj1=rectangle()
obj2=rectangle()
if(obj1<obj2):
    print("Object 2 is greater");
else:
    print("object 1 is greater");
    

    