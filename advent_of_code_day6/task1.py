def lantern_fish():
    with open('input.txt', 'r') as f:
        num_input = [int(i) for i in f.readlines()[0].split(",")]

    days = 80

    tmp = num_input
    while(days > 0):
        for i, val in enumerate(tmp):
            if val == 0:
                tmp[i] = 6
                tmp.append(9)
            else:
                tmp[i] = val - 1
        days = days - 1

    return len(tmp)

print(lantern_fish())