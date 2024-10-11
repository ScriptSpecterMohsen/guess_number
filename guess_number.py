# 1) user inout => low and high bound
# 2)random => [a,b]
# 3)loop => condition => =5 => feedback
import random

try:
    low = int(input("enter lower bound:"))
    high = int(input("enter high bound:"))
except ValueError:
    print("please enter a valid number:")
    low = int(input("enter lower bound:"))
    high = int(input("enter high bound:"))
R = random.randint(low, high)
guess_count = 5
guesses = []
while guess_count > 0:
    try:
        new_guess_str = input(f"remained guess: {guess_count} => enter a next guess:")
        new_guess =int(new_guess_str)

        if R == new_guess:
            print("Great! you guessed the right number!")
            break
        else:
            guesses.append(new_guess)
            if R > new_guess:
                print("your guess is lower than selected number")
            else:
                print("your guess is higher than selected number")
        guess_count -= 1
    except:
        print("please enter a valid number:")

if guess_count == 0:
    print(f"Your guess was wrong because {R} != {guesses} ")
