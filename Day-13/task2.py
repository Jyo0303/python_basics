class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def status(self):
        if self.marks >40:
            return "Passed"
             
        else:
            return "Failed"

    def display(self):
        result=self.status()
        print(f"Student: {self.name}\nRoll No: {self.roll_no}\nMarks: {self.marks}\nStatus: {result}")
    
name= input("enter the name: ")
roll_no = int(input("enter the roll number: "))
marks=int(input("enter the mark: "))
d1=Student(name,roll_no,marks)
d1.display()

