import random


def choices_function():
	

#game instruction
  print('Welcome player!\n'
	+'Rules of the game: \n'
	+'Rock and Paper- Paper wins \n'
	+'Rock and Scissors- Rock wins \n'
	+'Scissors and Paper- Scissors wins \n'
	+'Same choice- Tie \n')


#set players
choices = ['Rock', 'Paper', 'Scissors']

player1 = input( 'Rock, Paper or Scissors:') 
player2 = random.choice(choices)


#compare player1 input with player2 input

#if input is rock
if player1 == 'Rock':
    if player2 == 'Rock':
      results = print('%s vs. %s: Tie!' % (player1, player2 ))
    elif player2 == 'Paper':
      results = print('%s vs. %s: You lose' % (player1, player2))
    elif player2 == 'Scissors':
      results = print('%s vs. %s: You win' % (player1, player2))

#if input is paper
elif player1 == 'Paper':
    if player2 == 'Rock':
      results = print('%s vs. %s: You win' % (player1, player2))
    elif player2 == 'Paper':
      results = print('%s vs. %s: Tie!' % (player1, player2))
    elif player2 == 'Scissors':
      results = print('%s vs. %s: You lose' % (player1, player2))

#user's answer is scissors
elif player1 == 'Scissors':
    if player2 == 'Rock':
      results = print('%s vs. %s: You lose' % (player1, player2))
    elif player2 == 'Paper':
     results = print('%s vs. %s: You win' % (player1, player2))
    elif player2 == 'Scissors':
     results = print('%s vs. %s: Tie!' % (player1, player2))


else:
	print('invalid choice, try again')


while True:
	if input('Do you want to play again?') == "yes":
		choices_function()
	else:
	 print('Thank you for playing!')
	 break
  

choices_function()


