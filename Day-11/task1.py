import random
choose=0

while choose != 4:
    print("1. Roll a 6-sided die\n2. Roll a 20-sided die\n3. Roll multiple dice\n4. Exit\n")
    choose=int(input("Choose option: "))
    if choose==1:
        dice=random.randint(1,6)
        print(f"🎲 You rolled: {dice}")
    elif choose==2:
        dice=random.randint(1,20)
        print(f"🎲 You rolled: {dice}")
    elif choose==3:
        number_dice=int(input("How many dice? "))
        total=0
        dice_list=[]
        for i in range(number_dice):
            dice_list.append(random.randint(1,7))
            total+=dice_list[i]
        print(f"🎲 You rolled: {dice_list}")
        print(f"Total: {total}")
    elif choose==4:
        break
    else:
        print("correct option")
