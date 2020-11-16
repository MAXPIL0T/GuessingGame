import random

def guess(number, guess_allowed):
    guess_nr = int(input("Take a guess. "))
    if guess_nr == number:
        print("Your guess of {} is correct.\nYou winn!".format(guess_nr))
        guess_ct = guess_allowed + 1
        won = True
        return guess_ct, won
    elif guess_nr > number:
        print("Your guess of {} is too large!".format(guess_nr))
        won = False
        return won
    else:
        print("Your guess of {} is too small".format(guess_nr))
        won = False
        return won


won = False
guess_ct = 0
guess_allowed = 10
max_number = 50
number = random.randint(0, max_number)
print("Welcome to the number guess game!\nYou have to guess the number between 0 and {}.\nYou have {} attempts.\nYou can change these values by changing the max_number and guess_allowed fields.\nHave fun and good luck!\n".format(max_number, guess_allowed))

while guess_ct < guess_allowed:
    won = guess(number, guess_allowed)
    guess_ct += 1
    if won == False:
        print("You have {} guesses remaining\n".format(guess_allowed - guess_ct))

if won == False:
    print("You loose, the number was {}.".format(number))

input("Press enter to exit.")