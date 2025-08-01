def pal(name,left,right):
    if name[left]!= name[right]:
        return False
    elif left>=right:
        return True
    return pal(name,left+1,right-1)

name=input("Enter a word: ")
if pal(name,0,len(name)-1) == True:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
