queen_board = [[0, 1, 1, 1],
               [1, 0, 1, 1],
               [1, 0, 1, 1],
               [1, 1, 1, 0]]

def horizontal():
    print("Horizontal (rows):")
    for row in queen_board:
        print(row)

def vertical():
    print("Vertical (columns):")
    for j in range(len(queen_board[0])):
        col = [] 
        for i in range(len(queen_board)):
            col.append(queen_board[i][j])
        print(col)

def left_diagonal():
    print("Left Diagonal (main):")
    diag = []
    for i in range(len(queen_board)):
        diag.append(queen_board[i][i])
    print(diag)

print('In which dimension do you want to search?')
print('1. Horizontal')
print('2. Vertical') 
print('3. Left Diagonal')
user = input()

if user == '1':
    horizontal()
elif user == '2':
    vertical()
elif user == '3':
    left_diagonal()
else:
    print('Invalid option!')
