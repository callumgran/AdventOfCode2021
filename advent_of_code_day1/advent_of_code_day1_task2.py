measurements = []

def measurement_finder():
    counter = 0
    with open('measurements.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            measurements.append(int(line))

    last = measurements[0]
    mid = measurements[1]
    first = measurements[2]
    prev = last + mid + first

    sum = 0
    total = 0

    for i in measurements[3:]:
        last = mid
        mid = first
        first = i
        new = last + mid + first
        if new > prev:
            counter += 1

        prev = new

    return counter;

print(measurement_finder())