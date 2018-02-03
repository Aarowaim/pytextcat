from pytextcat import TextCatalog
import random
import os

# find hangman game data
game_files = []
for fname in os.listdir('.'):
    if fname.endswith('.hman'):
        game_files.append(fname)

while True:
    print('Please choose a file from the list:')

    for i, fname in enumerate(game_files):
        print('{})  {}'.format(i, fname))
    try:
        selection = int(input())
        if not 0 <= selection < len(game_files):

            raise ValueError('{} does not correspond to a file'
                             .format(selection))
        break

    except ValueError as e:
        print('\n' + str(e))

game_data = TextCatalog(game_files[selection])
substitutions = [[] for i in range(10)]

# find numbers to substitute in the ascii art
for i, c in enumerate(game_data['steps']):
    try:
        substitutions[int(c)].append(i)
    except ValueError:
        pass

# prepare game state
word = random.choice(game_data['words'].split())
attempts = 5
guesses = set()

# begin game
while attempts > 0:

    # Generate the gallows image
    gallows = game_data['steps']
    for k, v in enumerate(substitutions):
        for text_position in substitutions[k]:
            sub = ' ' if 5 - attempts <= k \
                    else game_data['gallows'][text_position]

            gallows = gallows[:text_position] + sub + gallows[text_position+1:]
    print(gallows)

    # Print status information
    print(''.join(c if c in guesses else '_' for c in word))
    print('Attempts:', attempts)

    # Get player guess
    while True:
        try:
            guess = input('Please enter a guess: ')
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError('Please enter a single letter')
            if guess in guesses:
                raise ValueError('You\'ve already guessed {}'.format(guess))
            break
        except ValueError as e:
            print('\n' + str(e))

    guesses.add(guess)

    if guess not in word:
        attempts -= 1

    # End guessing if the player found the word
    if set(word) <= guesses:
        break

# Print a result message for the player
if set(word) <= guesses:
    print(game_data['win'])
else:
    print(game_data['gallows'])
    print('He ded...')
