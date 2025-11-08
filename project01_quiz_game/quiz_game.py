print('Welcome to my computer quizz!')

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input('What is the capital of Mexico? ')
if answer.lower() == 'mexico city' or answer.lower() == 'cdmx' or answer.lower() == 'ciudad de mexico':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What is the capital of the USA? ')
if answer.lower() == 'washington dc' or answer.lower() == 'washington d. c.' or answer.lower() == 'washington d.c.':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What is the capital of Peru? ')
if answer.lower() == 'lima':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What is the capital of Argentina? ')
if answer.lower() == 'buenos aires':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What is the capital of China? ')
if answer.lower() == 'beijing':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + " questions correct!")
print('You got ' + str((score / 5) * 100) + "%.")