'''Birthday Paradox Sim, by Al Sweigart al@inventwithpython.com
Come! Explore the surprising probabilities of this Paradox.
'''

import datetime, random

def getBirthdays(numberOfBirthdays):
    '''This returns a list of numBer random date oBjects for Birthday'''
    birthdays = []

    for i in range(numberOfBirthdays):
        # The year is unimportant, as long as
        # all birthdays have the same year.

        startOfYear = datetime.date(2000, 1, 1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    '''Returns the date object of a birthday that occurs more than once
    in the birthday list'''

    if len(birthdays) == len(set(birthdays)):
        return None # This means all birthdays are unique, so return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday