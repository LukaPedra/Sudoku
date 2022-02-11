Board = [
    [0,0,0,0,0,0,0,0,0],
    [5,9,0,0,3,4,6,0,0],
	[0,6,0,0,0,0,0,8,0],
    [4,0,0,0,0,8,0,0,9],
    [0,1,0,0,0,0,0,7,6],
    [0,0,0,0,0,0,5,0,0],
    [0,7,0,9,0,0,0,0,3],
    [3,0,0,8,0,0,2,6,0],
    [0,5,0,0,7,0,0,0,0]
]

def valid(Board, n, pos):
	#row
	for i in range(len(Board[0])):
		if Board[pos[0]][i] == n and pos[1] != i:
			return False
	
	#column
	for i in range(len(Board)):
		if Board[i][pos[1]] == n and pos[1] != i:
			return False
	#Check box
	Caixa_x = pos[1] // 3
	Caixa_y = pos[0] // 3

	for i in range(Caixa_x* 3, Caixa_x*3 +3):
		for j in range(Caixa_y* 3, Caixa_y*3 +3):
			if Board[i][j] == n and (i,j) != pos:
				return False
	return True
				

def printBoard(Board):
	for i in range(len(Board)):
		if i % 3 == 0:
			print(" - - - - - - - - - - - - - -")
		
		for j in range(len(Board[0])):
			if j % 3 == 0:
				print(" | ",end="")
			if j == 8:
				print(Board[i][j])
			else:
				print(str(Board[i][j])+" ", end="")
def GetEmpty(Board):
	for i in range(len(Board)):
		for j in range(len(Board[0])):
			if Board[i][j] == 0:
				return (i,j)

printBoard(Board)
print(GetEmpty(Board))