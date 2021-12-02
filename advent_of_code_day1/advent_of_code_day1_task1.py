measurements = []

def measurement_finder():
    counter = 0
    with open('measurements.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            measurements.append(int(line))

    prev = measurements[0]

    for i in measurements[1:]:
        if i > prev:
            counter += 1;
        prev = i
    return counter;

print(measurement_finder())