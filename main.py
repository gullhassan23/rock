import random

def start():
    user = input("'r' for rock, 'p' for paper, 's' for scissor ")
    computer = random.choice(['r', 's', 'p'])
    print("you choice is " + user)
    print("computer choice is " + computer)


    if user == computer:
        return  'game is tie'


    if is_win(user,computer):

        return "you won"

    return "you lose"


def is_win(p,c):
    if(p == 'r' and c == 's') \
        or (p == 's' and c == 'p') \
        or(p == 'p' and c == 'r'):
     return True



game_result=start()
print(game_result)

