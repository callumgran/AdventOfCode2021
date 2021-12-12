with open('numbers.txt', 'r') as f:
    num_input, *board_input = f.read().split('\n\n')

def create_boards(num_input, board_input):
    nums = map(int, num_input.split(','))
    boards = []
    for board in board_input:
        rows = [[int(i) for i in row.split()] for row in board.split('\n')]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return nums, boards

def find_winning_board():
    nums, boards = create_boards(num_input, board_input)
    for num in nums:
        print(num)
        for i, board in enumerate(boards):
            if board is not None:
                if {num} in board:
                    print("cock")
                    winner = find_sum(board, num)
                    boards[i] = None
                    if i%2:
                        boards[i-1] = None
                    else:
                        boards[i+1] = None
                else:
                    boards[i] = [group.difference({num}) for group in board]
    return winner

def find_sum(board, num):
    return (sum(sum(group) for group in board) - num) * num

print(find_winning_board())