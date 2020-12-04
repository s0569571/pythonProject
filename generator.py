print('This is just a simple programm')

import random as rn


while True:
    rnd_num = rn.randint(1, 5)
    guess = 5
    if guess == rnd_num:
        print('damn u slick - num: ' + str(rnd_num))
        break
    else:
        print('u kinda dogshit - num: ' + str(rnd_num))
        continue

print("u won wohooooo!")