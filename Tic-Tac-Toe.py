def draw(board):
	for row in range(0,3):
		for col in range(0,3):
			print(board[row][col], end="")
		print('')

def pl_name(pl):
	if(pl[0] == 1):
		pl.append(input("Player 1's name: "))
	if(pl[0] == 2):
		pl.append(input("Player 2's name: "))

def check_range():
	num = input("Please provide a number between 1 and 3: ")
	while(1):
		if(num == '1' or num == '2' or num == '3'):
			return num
		else:
			num = input("Please provide correct input: ")
		

def select(board, pl):
	tf = 'n'
	while(tf == 'n'):
		print("Player ", pl[1], " turn")
		print("For the row")
		row = check_range()
		print("For the column")
		col = check_range()
		if(board[int(row) - 1][int(col) - 1] == " X " or board[int(row) - 1][int(col) - 1] == " O "):
			print('')
			print("PLEASE SELECT AGAIN THAT POSITION IS ALREADY TAKEN")
			print('')
		if(board[int(row) - 1][int(col) - 1] != " X " and board[int(row) - 1][int(col) - 1] != " O "):
			if(pl[0] == 1):
				board[int(row) - 1][int(col) - 1] = " X "
			if(pl[0] == 2):
				board[int(row) - 1][int(col) - 1] = " O "
			tf = 'y'

def three_row(board):
	countx = 0
	counto = 0
	for row in range(0,3):
		for col in range(0,3):
			if(board[row][col] == " X "):
				countx += 1
			if(board[row][col] == " O "):
				counto += 1
		if(countx == 3):
			return 1
		if(counto == 3):
			return 2
		countx = 0
		counto = 0
	return 0

def three_col(board):
	countx = 0
	counto = 0
	for col in range(0,3):
		for row in range(0,3):
			if(board[row][col] == " X "):
				countx += 1
			if(board[row][col] == " O "):
				counto += 1
		if(countx == 3):
			return 1
		if(counto == 3):
			return 2
		countx = 0
		counto = 0
	return 0

def three_diag(board):
	countx = 0
	counto = 0
	if(board[0][0] == " X " and board[1][1] == " X " and board[2][2] == " X "):
		return 1
	if(board[0][2] == " X " and board[1][1] == " X " and board[2][0] == " X "):
		return 1
	if(board[0][0] == " O " and board[1][1] == " O " and board[2][2] == " O "):
		return 2
	if(board[0][2] == " O " and board[1][1] == " O " and board[2][0] == " O "):
		return 2
	return 0

def won(board, pl1, pl2):
	if(three_row(board) == 1 or three_col(board) == 1 or three_diag(board) == 1):
		return 1
	if(three_row(board) == 2 or three_col(board) == 2 or three_diag(board) == 2):
		return 2
	if(three_row(board) == 0 and three_col(board) == 0 and  three_diag(board) == 0):
		return 0

def rounds(board, pl1, pl2):
	rcount = 0
	while(rcount != 8):
		if(rcount == 0 or rcount % 2 != 0):
			draw(board)
			select(board, pl1)
		if(rcount % 2 == 0):
			draw(board)
			select(board, pl2)
		if(won(board, pl1, pl2) == 1):
			print('')
			print("Player ", pl1[1], " has WON!")
			print('')
			break
		if(won(board, pl1, pl2) == 2):
			print('')
			print("Player ", pl2[1], " has WON!")
			print('')
			break
		rcount += 1
	if(won(board, pl1, pl2) == 0):
			print('')
			print("It was a tie")
			print('')
		
def check_str():
	tf = 'n'
	while(tf == 'n'):
		string = input("")
		if(len(string) == 1):
			if(string[0] == 'y' or string[0] == 'n'):
				return string
		print("Please say either y or n for yes or no")
def main():
	tf = 'n'
	roundnum = 1
	p1 = [1]
	p2 = [2]
	pl_name(p1)
	pl_name(p2)
	while(tf == 'n'):
		board = [[" * "] * 3, [" * "] * 3, [" * "] * 3]
		print("This is round", roundnum)
		rounds(board, p1, p2)
		roundnum += 1
		print("Would you like to play again? y or n")
		ans = check_str()
		if(ans == 'n'):
			tf = 'y'	
main()
