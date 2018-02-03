from pytextcat import TextCatalog
import random
import os


# find hangman game data
game_files = []
current_dir = os.path.dirname(os.path.abspath(__file__))
for fname in os.listdir(current_dir):
    if fname.endswith('.hman'):
        game_files.append(fname)


# Prompt player to choose game data for the theme
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


# Load the selected theme
fname = os.path.join(current_dir, game_files[selection])
game_data = TextCatalog(fname)


# find numbers to be substituted in the ascii art
substitutions = [[] for i in range(10)]
for i, c in enumerate(game_data['steps']):
    try:
        substitutions[int(c)].append(i)
    except ValueError:
        pass


# prepare game state
word = random.choice(game_data['words'].split())

highest_step = None
for i in reversed(range(10)):
    if len(substitutions[i]) > 0:
        highest_step = i
        break

allowed_attempts = highest_step if highest_step else 5
failures = 0
guesses = set()


# begin game
while failures <= allowed_attempts:

    # Generate the gallows image
    gallows = game_data['steps']
    for k, v in enumerate(substitutions):
        for text_position in substitutions[k]:
            sub = ' ' if failures <= k \
                    else game_data['gallows'][text_position]

            gallows = gallows[:text_position] + sub + gallows[text_position+1:]
    print(gallows)

    # Print status information
    print(''.join(c if c in guesses else '_' for c in word))
    print('Remaining:', allowed_attempts - failures)

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
        failures += 1

    # End guessing if the player found the word
    if set(word) <= guesses:
        break

# Print a result message for the player
if set(word) <= guesses:
    print(game_data['win'])
else:
    print(game_data['gallows'])
    print('He ded...')
