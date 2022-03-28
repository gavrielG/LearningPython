n1 = int(input("Enter 2 digit number: "))

while 10 <= n1 <=99:
    if n1 % 10 == 7 or n1 % 7 == 0 or n1 // 10 == 7:
        print("Lucky Number!")
    n1 = int(input("Enter 2 digit number: "))

