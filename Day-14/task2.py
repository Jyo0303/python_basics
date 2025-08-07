class Shape:
    
    def measure(self):
        self.radius=float(input("enter the circle radius: "))
        self.side=float(input("enter the side of the square: "))
        self.length=float(input("enter the length of rectangle: "))
        self.breadth=float(input("enter the breadth of rectangle: "))

class Circle(Shape):
    def area(self):
        a= 3.14*self.radius**2
        print(f"Circle Area: {a}")

class Square(Shape):
    def area(self):
        a=self.side*self.side
        print(f"Square Area: {a}")

class Rectangle(Shape):
    def area(self):
        a= self.length*self.breadth
        print(f"Rectangle Area: {a}")

s=Shape()
s.measure()

c=Circle()
c.radius=s.radius

sq=Square()
sq.side=s.side

r=Rectangle()
r.length=s.length
r.breadth=s.breadth

for i in [c,sq,r]:
    i.area()

