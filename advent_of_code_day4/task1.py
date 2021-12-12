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
        for i, board in enumerate(boards):
            if {num} in board:
                return find_sum(board, num)
            else:
                boards[i] = [group.difference({num}) for group in board]

def find_sum(board, num):
    return (sum(sum(group) for group in board) - num) * num

print(find_winning_board())