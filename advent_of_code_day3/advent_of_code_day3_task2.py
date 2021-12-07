def oxygenCarbonFinder():
    binary = []
    with open('binary.txt', 'r') as f:
        Lines = f.readlines()
        for line in Lines:
            binary.append(line.rstrip('\n'))

    arrOxygen = binary
    arrCarbon = binary
    for i, number in enumerate(binary):
        oxygen = []
        oneCounter = 0
        for numbers in arrOxygen:
            if numbers[i] == "1":
                oneCounter += 1

        for element in arrOxygen:
            if oneCounter >= len(arrOxygen)/2:
                if element[i] == "1":
                    oxygen.append(element)
            else:
                if element[i] == "0":
                    oxygen.append(element)

        arrOxygen = oxygen

        if len(arrOxygen) == 1:
            break

    for i, number in enumerate(binary):
        carbon = []
        oneCounter = 0
        for numbers in arrCarbon:
            if numbers[i] == "1":
                oneCounter += 1

        for element in arrCarbon:
            if len(arrCarbon) == 1:
                continue
            if oneCounter < len(arrCarbon)/2:
                if element[i] == "1":
                    carbon.append(element)
            else:
                if element[i] == "0":
                    carbon.append(element)

        arrCarbon = carbon

        if len(arrCarbon) == 1:
            break

    print(int(arrOxygen[0], 2))
    print(int(arrCarbon[0], 2))
    return int(arrCarbon[0], 2) * int(arrOxygen[0], 2)

print(oxygenCarbonFinder())