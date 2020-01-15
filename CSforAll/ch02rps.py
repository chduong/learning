# Unfair game of rock-paper-scissors
import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    running = True
    while running:
    # while True:
        user = input("Choose your weapon: ")
        comp = random.choice(['rock','paper','scissors'])
        print()

        print('The user (you)   chose', user)
        print('The computer (I) chose', comp)
        print()


        if user == 'rock' and comp == 'scissors':
            print('Ha! I really chose paper--I WIN!')
            print("Better luck next time...")

        elif user == 'paper' and comp == 'rock':
            print('Ha! I really chose scissors--I WIN!')
            print("Better luck next time...")

        elif user == 'scissors' and comp == 'paper':
            print('Ha! I really chose rock--I WIN!')
            print("Better luck next time...")

        elif user == comp:
                print('It\'s a tie!')

        # print('Comp still playing...')
        # response = input('Play again?')
        # if response == 'n':
        #     break

        print('Comp still playing...')
        response = input("Play again? ")
        if response == 'n':
            running = False

rps()