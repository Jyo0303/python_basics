def repeat(n,no):
    if n<=no:
        return
    print("*"*no)
    repeat(n,no+1)

repeat(5,1)
