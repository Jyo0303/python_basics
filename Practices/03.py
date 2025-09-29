# Write Python code to print only Alice’s Math marks.

students = {
    "Alice": [
        {"subject": "Math", "marks": 90},
        {"subject": "English", "marks": 85}
    ],
    "Bob": [
        {"subject": "Biology", "marks": 78},
        {"subject": "Chemistry", "marks": 88}
    ],
    "Charlie": [
        {"subject": "Physics", "marks": 92},
        {"subject": "Math", "marks": 80}
    ]
}
for i in students["Alice"]:
    if i["subject"]=="Math":
        print(f"marks:{i['marks']}")
