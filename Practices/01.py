# Question:
# Write Python code to print the department of Sara.

employees = [
    {"name": "John", "age": 25, "dept": "HR"},
    {"name": "Sara", "age": 28, "dept": "IT"},
    {"name": "Mike", "age": 30, "dept": "Finance"}
]
for i in employees:
    if i["name"]=="Sara":
        print(i["dept"])
