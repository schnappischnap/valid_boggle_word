import re

DICE = ['DIYSTT',
        'NMIQUH',
        'RLVEDY',
        'OTMICU',
        'AOSCPH',
        'IENSUE',
        'FAKPSF',
        'EVWHTR',
        'OOBJBA',
        'NAEAEG',
        'RLTYTE',
        'ZNRNLH',
        'DEXLRI',
        'AOTTOW',
        'GEWHEN',
        'ESTISO']


def dice_with_char(char, *dice):
    for die in dice:
        if char in die:
            yield die


def next_letter(word, dice_left, dice_used=None, level=0):
    dice_left = list(dice_left)  # make a deep copy of dice_left
    if dice_used is None:
        dice_used = []

    if level == len(word):  # word completed
        return dice_used

    for die in dice_with_char(word[level], *dice_left):
        dice_left.remove(die)
        dice_used.append(die)

        if next_letter(word, dice_left, dice_used, level+1):
            return dice_used

        dice_used.remove(die)
        dice_left.append(die)

    return False  # word cannot be made from the dice


def solve(word):
    word = word.upper().replace(' ', '')

    if re.search(r'[^A-Z]', word):
        print("Input must only contain letters.")
        return
    if re.search(r'Q($|[^U])', word):
        print("'Q' must always be followed by 'U'.")
        return
    if len(word) > 16 + sum(char == 'Q' for char in word):
        print("{} is too long.".format(word))
        return

    word = re.sub(r'QU', 'U', word)  # remove any U's succeeding a Q

    result = next_letter(word, DICE)
    print(result if result else "Word cannot be made.")


while True:
    solve(input("> "))
    print()
