'''
guess number from 1 to 100
easy mode 10  tries
hard mode 5 tries


'''

from random import randint

# pick the number
the_number = randint(1,100)

# determine mode and set tries
mode = input("'easy' mode or 'hard' mode? ")
tries = 0 
if mode == 'easy':
    tries = 10
else: 
    tries = 5

playing = True
while playing:
    print(f"\nyou have {tries} tries left.")
    guess_number = int(input("guess number: "))
    if guess_number > the_number:
        print('too high')
        tries -= 1
    elif guess_number<the_number:
        print('too low')
        tries -= 1
    else:
        print('you win')
        playing=False
    
    if tries == 0:
        print('you loose')
        playing=False


