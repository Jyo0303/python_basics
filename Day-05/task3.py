print("Shopping List Manager")
a=[]
while True:
    print("1. Add item\n2. Remove item\n3. Show list\n4. Check item\n5. Exit")
    c=int(input("Choice: "))
    if c==1:
        b=input("Enter item: ")
        a.append(b)
        print(f"Added {b} to the list!")
    elif c==2:
        b=input("which item is to be remove: ")
        d=a.remove(b)
        print(f"Removed {b} from the list!")
    elif c==3:
        print(f"Shopping list: {a}")
    elif c==4:
        print("Enter item that check: ")
        b=input()
        if b in a:
            d=a.index(b)
            print(f"{b} is in {d}th index ")
        else:
            print("enter correct item")
    elif c==5:
        print("Exit.........")
        break
    else:
        print("Enter correct choice ")
