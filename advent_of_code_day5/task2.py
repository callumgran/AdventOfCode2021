def create_coords():
    x_data = []
    y_data = []
    map = {}
    with open('input.txt', 'r') as f:
        num_input = f.read().split('\n')

    for num in num_input:
        coords = [[int(i) for i in coord.split(',')] for coord in num.split('->')]
        for i, coord in enumerate(coords):
            for j in range(len(coords[i])):
                if j == 0:
                    x_data.append(coords[i][j])
                else:
                    y_data.append(coords[i][j])

    x1_data = x_data[::2]
    x2_data = x_data[1::2]
    y1_data = y_data[::2]
    y2_data = y_data[1::2]
    rows, cols = (len(x_data), len(y_data))

    total = [[0]*cols]*rows

    for i in range(len(x1_data)):
        x_1 = x1_data[i]
        x_2 = x2_data[i]
        y_1 = y1_data[i]
        y_2 = y2_data[i]

        if x_1 == x_2:
            min_y = min(y_1, y_2)
            max_y = max(y_1, y_2)
            for i in range(max_y - min_y + 1):
                key = str(x_1) + "," + str(min_y + i)
                if key in map:
                    map[key] += 1
                else:
                    map[key] = 1

        elif y_1 == y_2:
            min_x = min(x_1, x_2)
            max_x = max(x_1, x_2)
            for i in range(max_x - min_x + 1):
                key = str(min_x + i) + "," + str(y_1)
                if key in map:
                    map[key] += 1
                else:
                    map[key] = 1

        else:
            x = x_1 < x_2
            y = y_1 < y_2

            for i in range(abs(x_1 - x_2) + 1):
                if x:
                    new_x = str(x_1 + i)
                else:
                    new_x = str(x_1 - i)
                if y:
                    new_y = str(y_1 + i)
                else:
                    new_y = str(y_1 - i)
                key = new_x + "," + new_y
                if key in map:
                    map[key] += 1
                else:
                    map[key] = 1

    sum = 0
    for val in map.values():
        if val >= 2:
            sum += 1

    return sum

print(create_coords())