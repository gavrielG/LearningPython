n1 = int(input("Enter 3 digit number: "))
while 100 <= n1 <= 999:
    print(f"{n1%10+n1//10%10+n1//100}")
    if n1 < 100 or n1 > 999:
        print("Invalid number")
    n1 = int(input("Enter 3 digit number: "))
print("Invalid number")
