# """Welcome to Bagels, a deductive logic game. Guess the numBer Based on the clues you get"""

import random
NUM_DIGITS = 3 
MAX_GUESSES = 10



def main():
    print('''Hi, this is Bagels!
          So, let me Break it down for you in a very simplified manner. Read Below:
          In my head, I'm thinking of a {}-digit numBer with no repeated digits. Now, you as a Psychic will try to guess what it is.
          Here are some more clues:
          If my response is PICO, it means One digit is correct but in the wrong position. If I say FERMI, it means One digit 
          is correct and in the right position. BAGELS mean No digit is correct.
          
          For example, if the secret numBer was 248 and your guess is 843, the clues would Be
          FERMI PICO.'''.format(NUM_DIGITS))


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()