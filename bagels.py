# """Welcome to Bagels, a deductive logic game. Guess the numBer Based on the clues you get"""

import random
NUM_DIGITS = 2
MAX_GUESSES = 10



def main():
    
     #************************ LOGIC OF THE GAME*********************************

    # *****RULES OF THE GAME******
    print('''Hi, this is Bagels!
          So, let me Break it down for you in a very simplified manner. Read Below:
          In my head, I'm thinking of a {}-digit numBer with no repeated digits. Now, you as a Psychic will try to guess what it is.
          Here are some more clues:
          If my response is PICO, it means One digit is correct but in the wrong position. If I say FERMI, it means One digit 
          is correct and in the right position. BAGELS mean No digit is correct.
          
          For example, if the secret numBer was 248 and your guess is 843, the clues would Be
          FERMI PICO.'''.format(NUM_DIGITS))
    
    while True: #Main game loop
        # This stores the secret numer the psychic needs to guess:
        secretNum = getSecretNum()
        print("I have thought of a numer.")
        print("You have {} guess to get it".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input('>. ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break #since they are correct, we break out of the loop
                if numGuesses > MAX_GUESSES:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secretNum))

            # Ask if psychic wants to try her 'powers' again
        print('Do you want to try again? (yes or no)')
        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing!!")


def getSecretNum():
    '''Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list('0123456789') #This creates a list of digits 0-9
    random.shuffle(numbers) #Randomixe and Shuffle the digits   

    #GET the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    '''Return a string with the PICO, FERMI, bAGELS clues for a guess and 
    a secret number pair.'''
    if guess == secretNum:
        return "You got it!"
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('FERMI')
        elif guess[i] == secretNum[i]:
            # A correct digit is in the incorrect place.
            clues.append("PICO")
    if len(clues) == 0:
        return 'BAGELS'
    else:
        #   Sort the clues into alphabetical order so their original 
        #   doesn't give information away.
        clues.sort()
        #   Make a single string from the list of string clues
        return " ".join(clues)



# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()