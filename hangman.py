from random import randint

def print_board(guess_number, board_dict):
	print()
	print(' ----|')
	
	line1 = 0
	line2 = 0
	line3 = 0

	if guess_number > 0:
		for x in range(1,guess_number+1):
			if x==1:
				line1 = x
				continue
			if x==2 or x==3 or x==4:
				line2 = x
				continue
			if x==5 or x==6:
				line3 = x
				continue

	print(board_dict[str(line1)])
	print(board_dict[str(line2)])
	print(board_dict[str(line3)])
	print(' |')
	print('---')

def get_random_word(words):

	rand_word = words[randint(0,len(words))]
	disp_word = ['_' for _ in rand_word]

	game_words = {'word': rand_word, 'guess': disp_word}

	return(game_words)

# create list from text file
words = []
with open('random_words.txt') as w:
	words = ''.join(w.readlines()).split()

# this is the dictionary for storing all of the stickman components
board_dict = {
	'0':' |',
	'1':' |   O',
	'2':' |   |',
	'3':' |  /|',
	'4':' |  /|\\',
	'5':' |  /',
	'6':' |  / \\'
}

play_game = True
guessed_letters = []
count = 0
game_words = get_random_word(words)
ask_play_again = False

while play_game:
	correct = False

	print_board(count, board_dict)
	print(' '.join(guessed_letters))
	print(' '.join(game_words['guess']))

	user_guess = input('Enter a letter: ')
	print()

	print('Length of input is %d' % (len(user_guess)))

	if not user_guess.isalpha() or not len(user_guess) ==1:
		print('Only single letters allowed!')
	else:
		if user_guess in guessed_letters or user_guess in game_words['guess']:
			print('Letter already guessed!')
		else:
			for index,a in enumerate(game_words['word']):
				if user_guess == a:
					game_words['guess'][index] = user_guess
					correct = True
		
			if not correct:
				count += 1
				guessed_letters.append(user_guess)

			if count == 6:
				print_board(count, board_dict)
				print('You lost!')
				print('Correct word was %s' %(game_words['word']))
				ask_play_again = True

			if game_words['word'] == ''.join(game_words['guess']):
				print('You win!!')
				ask_play_again = True

			if ask_play_again:	
				choice = input('Play again? y/n ')
				if choice == 'y':
					count = 0
					game_words = get_random_word(words)
					guessed_letters = []
				else:
					play_game = False
					print('Bye yo!')
				ask_play_again = False

