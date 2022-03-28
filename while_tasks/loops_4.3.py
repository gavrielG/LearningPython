from random import randint

n1 = randint(1, 9)

n2 = int(input("Guess the number 1-9: "))

while n2 < n1:
    print("Higher")
    n2 = int(input("Guess the number 1-9: "))

while n2 > n1:
    print("Lower")
    n2 = int(input("Guess the number 1-9: "))
if n2 == n1:
    print("Right answer!")

# =========================================================================================

# while n2 > 9 or n2 < 1:
#     print("Invalid number, try again.")
#     n2 = int(input("Guess the number 1-9: "))
#
# while 1 <= n2 <= 9:
#     if n2 == n1:
#         print("Correct!")
#
#     if n2 < n1:
#         print("Higher")
#
#     if n2 > n1:
#         print("Lower")
#     n2 = int(input("Guess the number 1-9: "))
#






