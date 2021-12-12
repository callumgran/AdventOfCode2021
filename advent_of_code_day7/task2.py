def crab_subs():
    with open('input.txt', 'r') as f:
        num_input = [int(i) for i in f.readlines()[0].split(',')]
        start, end = min(num_input), max(num_input) + 1

    def get_cost(value, current_position):
        movecost = abs(value - current_position)
        return (movecost * (movecost + 1)) // 2

    costs = []
    for pos in range(start, end):
        costs.append(sum(get_cost(i, pos) for i in num_input))
    return min(costs)

print(crab_subs())