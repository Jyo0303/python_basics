def calc(l, w):
    p= 2 * (l + w)
    a = l * w
    print("Rectangle Calculator")
    print(f"Length: {l} ")
    print(f"width: {w}")
    print(f"Perimeter: {p}")
    print(f"Area: {a}")
    
l=int(input("enter Length: "))
w=int(input("enter width: "))
calc(l, w)
