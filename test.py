import random
from words import words


def Game():

    guess = words [random.randint(0, 4)]

    print (guess)

    prompt = input("please select either please, apple, orange, pear, tree : ")

    if prompt == guess :
        result = "Well done \"{}\" is the right answer.".format(guess)
        print (result)
    else :
        print("you got it wrong, the right answer is: \"" + guess +"\"" )



Game()

running = True

while running == True:

    Play_again= input("Do you want to play again : ")

    if Play_again == "yes":
        Game()
    else:
        print("Thank you for playing!")
        running = False
