movements = []

def movement_finder():
    counter = 0
    with open('movements.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            movements.append(line)

    lateral = 0
    vertical = 0

    for i in movements:
        if "forward" in i:
            for word in i.split():
                if word.isdigit():
                    lateral += int(word)
        elif "up" in i:
            for word in i.split():
                if word.isdigit():
                    vertical -= int(word)
        elif "down" in i:
            for word in i.split():
                if word.isdigit():
                    vertical += int(word)

    return lateral * vertical

print(movement_finder())