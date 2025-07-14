def f_to_c(f):
    c=(f-32)*5/9
    return f"{f}°F is {c:.1f}°C"
f=int(input("Enter temperature in Fahrenheit: "))
print(f_to_c(f))
