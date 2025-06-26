import random

# say hello to the user
print("it's a number guessing game! type in a whole number between 1 and 100:")

# check that the user has entered a number or digit
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

# main function
def game():
    count = 1
    random_num = random.randint(1, 100)
    while True:
        num = input()
        if not is_valid(num):
            print("it doesn't look like an integer between 1 and 100")
            continue
        num = int(num)
        if num < random_num:
            print("your number is less than the number you guessed, try again")
            count += 1
        elif num > random_num:
            print("your number is higher than your guess, try again")
            count += 1
        else:
            print("you got it, good for you!")
            print(f"your attempts: {count}")
            break
game()

# a function that prompts the user to play again
def one_time():
    while True:
        print("can we play again? yes/no.")
        answer = input().strip().lower()
        if answer == 'yes':
            print("enter a number:")
            game()
        elif answer == 'no':
            print("okay, bye!")
            break
        else:
            print("that's not exactly what i was expecting.... okay, bye!")
            break
one_time()