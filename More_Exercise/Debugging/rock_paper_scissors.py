from random import randint

def win():
    print('You Win!')
def lose():
    print('You Lose')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    print(computer_choice)

    if player_choice==computer_choice:
        print ('Draw!')
    elif  player_choice == 'rock' and computer_choice == 'scissors':
        print('Win')
    elif  player_choice == 'paper' and computer_choice == 'scissors':
        print('Lose')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('Win')
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('Lose')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('Win')
    elif player_choice == 'rock' and computer_choice == 'paper':
        print('Lose')
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'n':
        break
win() 
lose()
        