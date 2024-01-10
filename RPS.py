import random

user_total_wins = 0
computer_total_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock, Paper, or Scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("The Computer picked:", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Congrats! You're a winner!")
        user_total_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Congrats! You're a winner!")
        user_total_wins += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("Congrats! You're a winner!")
        user_total_wins += 1

    elif user_input == computer_pick:
        print("It's a tie, try again.")

    else:
        print("Aw man! You lose.")
        computer_total_wins += 1

print("You won", user_total_wins, "times")
print("The Computer won", computer_total_wins, "times")
print('Thanks for playing!')