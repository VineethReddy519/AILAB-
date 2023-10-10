import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def computer_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move
def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0}
    if check_winner(board, 'O'):
        return scores['O']
    elif check_winner(board, 'X'):
        return scores['X']
    elif is_board_full(board):
        return scores['tie']
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        if current_player == 'X':
            row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
            if board[row - 1][col - 1] != ' ':
                print("Invalid move. Try again.")
                continue
            board[row - 1][col - 1] = current_player
        else:
            print("Computer's turn:")
            row, col = computer_move(board)
            board[row][col] = current_player
        print_board(board)
        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        current_player = 'X' if current_player == 'O' else 'O'
if __name__ == "__main__":
    play_game()
