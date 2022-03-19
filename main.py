import random

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a Tie!'

    if is_win(user, computer):
        return 'YOU WON!'

    return 'You lost :('

def is_win(player, opponent):
    # true if player wins
    if((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r')):
        return True

print(play())