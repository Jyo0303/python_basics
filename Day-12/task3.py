def fibo(n,first,second,count):
    print (first,end=" ")
    if count>n-1:
        return
    series=first+second
    
    fibo(n,second,series,count+1)

n=int(input("Enter how many terms: "))
first=0
second=1
count=1
fibo(n,first,second,count)
