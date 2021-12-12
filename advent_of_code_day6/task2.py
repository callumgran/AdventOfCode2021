def lantern_fish():
    with open('input.txt', 'r') as f:
        num_input = [int(i) for i in f.readlines()[0].split(",")]

    map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for i in num_input:
        map[i] += 1

    days = 256
    while(days > 1):
        tmp = {}
        for i, val in map.items():
            if i != 0:
                tmp[i - 1] = val
        tmp[9] = tmp[0]
        tmp[7] += tmp[0]
        map = tmp
        days = days - 1

        sum = 0
        for i, val in map.items():
            if i != 9:
                sum += val

    return sum

print(lantern_fish())