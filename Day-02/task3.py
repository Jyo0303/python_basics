n1=int(input("Enter first number: "))
o=input("Enter operation (+, -, *, /): ")
n2=int(input("Enter second number: "))
if o=="+":
    r=n1+n2
    Result=f"Result: {r}"
    print(Result)
elif o=="-":
    r=n1-n2
    Result=f"Result: {r}"
    print(Result)
elif o=="*":
    r=n1*n2
    Result=f"Result: {r}"
    print(Result)
else:
    r=n1/n2
    Result=f"Result: {r}"
    print(Result)
