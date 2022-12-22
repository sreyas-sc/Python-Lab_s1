class recatngle:
        length=0
        breadth=0
        def area(self):
            return self.length*self.breadth
        def perimeter(self):
            return 2*(self.length+self.breadth)
        def com(self,ob1):
            if self.area()>ob1.area():
                print("rectangle 1 is greater");
            else:
                print("rectangle 2 is greater");
r1=recatngle();
r1.length=int(input("Enter the length of rectangle 1: "))
r1.breadth=int(input("Enter the breadth of rectangle 1: "))
print(r1.area());
print(r1.perimeter());
r2=recatngle();
r2.length=int(input("Enter the length of rectangle 2: "))
r2.breadth=int(input("Enter the breadth of rectangle 2: "))
print(r2.area());
print(r2.perimeter());
r1.com(r2);
