student_score={"Alice": 95, "Bob": 87, "Carol": 92}
with open("Score_Tracker.txt","w") as file:
    file.write(f"High Scores Tracker\nCurrent high scores:\n\n")

    count=1
    for name,score in student_score.items():
        file.write(f"{count}. {name}: {score}\n")
        count+=1

with open("Score_Tracker.txt","r") as file:
    print(file.read())

name=input("Enter your name: ")
score=int(input("Enter your score: "))
student_score[name]=score


items = list(student_score.items())
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i]


with open("Score_Tracker.txt", "w") as file:
    file.write("High Scores Tracker\n")
    file.write("Updated high scores:\n\n")
    count = 1
    for name, score in items:
        file.write(f"{count}. {name}: {score}\n")
        count += 1


with open("Score_Tracker.txt", "r") as file:
    print(file.read())
