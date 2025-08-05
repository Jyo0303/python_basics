class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def summery(self):
        print(f"Book Summary:\nTitle: {self.title}\nAuthor: {self.author}\nPublished: {self.year}")
title=input("enter Title: ")
author=input("enter the author name: ")
year=int(input("enter the input year: "))

b1=Book(title,author,year)
b1.summery()
