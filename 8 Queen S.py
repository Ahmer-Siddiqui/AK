# Initial 4x4 board
Q_board = [
    [0, 0, 0, 0], #1.  [0][3 - 0]
    [1, 1, 1, 1], #2. [1][3 - 1] === [1][2]
    [0, 1, 0, 1], #3. [2][3-2] == [2][1]
    [1, 0, 1, 0]
]                   # 0 indicated Queen

players = ["A", "B"]
scores = {"A": 0, "B": 0}

def print_board():
    for row in Q_board:
        print(row)
    print()

def replace_vertical(col):
    replaced = 0
    for i in range(4):
        if Q_board[i][col] == 1:
            Q_board[i][col] = 0
            replaced += 1
            print("1 is replaced by 0 in vertical!")
    return replaced

def replace_horizontal(row):
    replaced = 0
    for j in range(4):
        if Q_board[row][j] == 1:
            Q_board[row][j] = 0
            replaced += 1
            print("1 is replaced by 0 in horizontal!")
    return replaced

def replace_left_diagonal():
    replaced = 0
    for i in range(4):
        if Q_board[i][i] == 1:
            Q_board[i][i] = 0
            replaced += 1
            print("1 is replaced by 0 in left diagonal!")
    return replaced

def replace_right_diagonal():
    replaced = 0
    for i in range(4):
        if Q_board[i][3 - i] == 1:
            Q_board[i][3 - i] = 0
            replaced += 1
            print("1 is replaced by 0 in right diagonal!")
    return replaced

def count_possible_moves():
    count = 0
    for row in Q_board:
        for cell in row:
            if cell == 1:
                count += 1
    return count


# Game loop for 4 turns per player
for turn in range(4):
    for player in players:
        print(f"\nPlayer {player}'s Turn")
        print_board()
        print("Possible moves:", count_possible_moves())

        if(count_possible_moves() == 0):
            print("\nNo possible move left !!\n")
            break

        print("---------------- Choose direction: ----------------")
        print("1. Vertical\n2. Horizontal\n3. Left Diagonal\n4. Right Diagonal")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            col = int(input("Enter column (0-3): "))
            score = replace_vertical(col)
        elif choice == 2:
            row = int(input("Enter row (0-3): "))
            score = replace_horizontal(row)
        elif choice == 3:
            score = replace_left_diagonal()
        elif choice == 4:
            score = replace_right_diagonal()
        else:
            print("Invalid choice!")
            score = 0

        scores[player] += score  # {'A':0, 'B': 0} 
        # scores['A'] --> 0  ==== scores['A'] += 2 -----> {'A': 2, 'B':0} 
        print(f"\nScore this turn: {score}")
        print(f"Total Score - A: {scores['A']} | B: {scores['B']}")
        print("-" * 30)
        print(f"turn {turn}")

print("Final Board:")
print_board()
print("Final Scores:")
print(f"Player A: {scores['A']}")
print(f"Player B: {scores['B']}")
if scores["A"] > scores["B"]:
    print("Player A wins!")
elif scores["B"] > scores["A"]:
    print("Player B wins!")
else:
    print("It's a tie!")