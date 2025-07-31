def add(n,summ):
    if n<=0:
        return summ
    summ+=n
    return add(n-1,summ)
n=int(input("Enter a number: "))
summ=0
sum_no=add(n,summ)
print(f"Sum from 1 to {n} is: {sum_no}")
