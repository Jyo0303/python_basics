try:
    choose="y"
    while choose.lower()=="y": 
        file_name=input("Enter filename: ")
        with open(file_name) as file:
            print(file.read())
        choose=input("Would you like to try another file? (y/n): ")

except FileNotFoundError:
    print("Error: File 'missing.txt' not found!") 
