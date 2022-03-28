from random import *

max_n = 100                                # Defining minimum and maximum boundaries of the randomly generated number
min_n = 0

counter = 0

print("Think of a number from 0 - 100.")

n = randint(min_n, max_n)

print(f"Did you think about {n}?")

answer = (input(f"If this number is correct type {0},\n"
                f"If this number is lower then yours type {1},\n"
                f"If this number is higher then yours type {2},\n"
                f"Answer: "))

if answer.isnumeric():                      # To check if the input is numeric
    answer = int(answer)                    # If the input is numeric it will convert to int
    counter += 1
    while answer != 0:                      # If the input is anything else then 0

        if min_n == max_n:                  # When Min and Max turn out to be the same number
            print("No options, Restart.")
            break                           # Ending the task

        else:
            if answer == 1:
                min_n = n+1                 # Turning the minimum number to one above what I got
                n = randint(min_n, max_n)
                print(f"Did you think about {n}?")

                answer = (input(f"If this number is correct type {0},\n"
                                f"If this number is lower then yours type {1},\n"
                                f"If this number is higher then yours type {2},\n"
                                f"Answer: "))
                if answer.isnumeric():      # To check if the answer is numeric
                    answer = int(answer)
                    counter += 1
                else:
                    print("Invalid answer.")
                    break
            elif answer == 2:
                max_n = n-1
                n = randint(min_n, max_n)
                print(f"Did you think about {n}?")

                answer = (input(f"If this number is correct type {0}\n"
                                f"If this number is lower then yours type {1},\n"
                                f"If this number is higher then yours type {2},\n"
                                f"Answer: "))
                if answer.isnumeric():
                    answer = int(answer)
                    counter += 1
                else:
                    print("Invalid answer.")
                    break
            elif answer > 2:
                print("Invalid answer.")
                answer = (input(f"If this number is correct type {0},\n"
                                f"If this number is lower then yours type {1},\n"
                                f"if this number is higher then yours type {2},\n"
                                f"Answer: "))
                if not answer.isnumeric():
                    break
    counter += 1
    print(f"Counter: {counter}")            # If the input is 0 -Line 21-
else:
    print("Invalid answer.")
