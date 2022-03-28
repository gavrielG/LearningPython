n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

while n1 % 2 == 0 and n2 % 2 == 0:
    print(f"{n1}+{n2}={n1+n2}")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
print(f"{n1}*{n2}={n1*n2}")
