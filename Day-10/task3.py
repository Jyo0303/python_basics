try:
    total=0
    avg=0
    print("Grade Calculator")
    no_grades = int(input("How many grades to enter? "))
    for i in range(no_grades):
        grade = int(input(f"Enter grade {i+1} (0-100): "))
        if 0 > grade or grade >100:
            print("Error: Grade must be between 0 and 100!")
            break
        total += grade
    
    avg = total / no_grades
    print(f"Average grade: {avg}")
    if avg >= 90:
        print("Letter grade: A")
    elif 80 <= avg < 90:
        print("Letter grade: B")
    elif 70 <= avg < 80:
        print("Letter grade: C")
    elif 60 <= avg < 70:
        print("Letter grade: D")
    elif 50 <= avg < 60:
        print("Letter grade: E")
    else:
        print("Failed")
  
except ValueError:
    print("Error: Please enter a valid number!")

