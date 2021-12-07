binary = []


def power_finder():
    gamma = []
    epsilon = []
    gammaBinary = ""
    epsilonBinary = ""
    with open('binary.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            binary.append(line.rstrip('\n'))

    for i in range(len(binary[0])):
        nullCounter = 0
        oneCounter = 0
        for j in range(len(binary)):
            if binary[j][i] == "0":
                nullCounter += 1
            elif binary[j][i] == "1":
                oneCounter += 1

        if nullCounter < oneCounter:
            epsilon.append(0)
            gamma.append(1)
        elif nullCounter > oneCounter:
            epsilon.append(1)
            gamma.append(0)

    for i in gamma:
        gammaBinary += str(i)

    for i in epsilon:
        epsilonBinary += str(i)

    return int(gammaBinary, 2) * int(epsilonBinary, 2)

print(power_finder())
