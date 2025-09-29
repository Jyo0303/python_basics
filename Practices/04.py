#Write Python code to print the highest grade of Bob.
grades = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [95, 100, 85]
}
lst=[]
lst = grades["Bob"]
largest = 0
for j in lst:
    if largest <= j:
        largest = j
print(largest)
