import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print('Computer picked ', computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You win!')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('You win!')
        user_wins += 1
    
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You win!')
        user_wins += 1
    
    elif user_input == computer_pick:
        print('It is a tie!')

    else:
        print('You lose!')
        computer_wins += 1

print('You won', user_wins, "times. ")
print('The computer won', computer_wins, 'times')
if user_wins > computer_wins:
    print('You won with a final score of', user_wins, ':', computer_wins)
elif computer_wins > user_wins:
    print('You lost with a final score of', user_wins, ':', computer_wins)
else:
    print('It is a tie! With a final score of', user_wins, ':', computer_wins)
print('Goodbye!')