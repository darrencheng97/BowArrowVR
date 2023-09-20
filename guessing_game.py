# Ask user to enter a number to guess the correct number
# if user enter the number is greater than the correct number, the game will ask user to enter smaller value number
# if user enter the number is smaller than the correct number, the game will ask user to enter greater value number

secret_num = 50
guess = None
guess_count = 0
guess_limit = 10
out_of_limit = False

print("Secret Number Guessing Game\n")
print("----------------------\n")
print("RULES\n")
print("Enter a number to guess the correct secret number.\nYou have 10 times of guess limit.\nOnce you exceed the limit you will lose the game. \nAll the best!\n")

while (guess != secret_num and not(out_of_limit)):
    if (guess_count <= guess_limit):
        guess_count+=1
        guess = int(input("Please enter a number:"))
        if guess > secret_num:
            print("Smaller a bit.")
        elif guess < secret_num:
            print("Greater a bit.")
    else:
        out_of_limit = True

if out_of_limit:
    print("Game Over! You have exceed the guess limit.")
else:
    print("Congratulations!! You have guesse the secret number correctly!")