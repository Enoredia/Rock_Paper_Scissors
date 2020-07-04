import random

#game instruction
print('Welcome player!\n'
	+'Rules of the game: \n'
	+'Rock and Paper- Paper wins \n'
	+'Rock and Scissors- Rock wins \n'
	+'Scissors and Paper- Scissors wins \n'
	+'Same choice- Tie \n')

#set players

choices = ['ROCK', 'PAPER', 'SCISSORS']
	

def game():
	player1 = input('Rock, Paper or Scissors:')
	player1 = player1.upper()
	player2 = random.choice(choices)

#compare player1 input with player2 input
#if input is rock
	if player1.upper() == 'ROCK':
		if player2 == 'ROCK':
			results = print('%s vs. %s: Tie!' % (player1, player2 ))
		elif player2 == 'PAPER':
			results = print('%s vs. %s: You lose' % (player1, player2))
		elif player2 == 'SCISSORS':
			results = print('%s vs. %s: You win' % (player1, player2))


        #if input is paper
	elif player1.upper() == 'PAPER':
		if player2 == 'ROCK':
			results = print('%s vs. %s: You win' % (player1, player2))
		elif player2 == 'PAPER':
			results = print('%s vs. %s: Tie!' % (player1, player2))
		elif player2 == 'SCISSORS':
			results = print('%s vs. %s: You lose' % (player1, player2))

        #user's answer is scissors
	elif player1.upper() == 'SCISSORS':
		if player2 == 'ROCK':
			results = print('%s vs. %s: You lose' % (player1, player2))
		elif player2 == 'PAPER':
			results = print('%s vs. %s: You win' % (player1, player2))
		elif player2 == 'SCISSORS':
			results = print('%s vs. %s: Tie!' % (player1, player2))

	else:
			print('invalid choice, try again')


def choices_function():
	game()
	while True:
		if input('Do you want to play again?') == "yes":
			game()
		else:
			print('Thank you for playing!')
			break
  

choices_function()

