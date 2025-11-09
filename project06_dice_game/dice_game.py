import random

def roll():
    roll = random.randint(1, 6)
    return roll

while True:
    players = input('Enter the number of players (2 - 4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print('Must be between 2 to 4 players.')
    else:
        print('Invalid, try again.')

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f'\n\nPlayer {player_idx + 1}\'s turn has started')
        print(f'Your total score is: {player_scores[player_idx]}\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll? ')
            if should_roll.lower() not in ['y' or 'yes' or 'yeah']:
                break

            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'Your current score is: {current_score}')
        
        player_scores[player_idx] += current_score
        print(f'Your total score is: {player_scores[player_idx]}')

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f'Player {winning_idx + 1} wins with a score of: {max_score}')