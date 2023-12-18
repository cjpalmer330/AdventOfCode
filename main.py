import fileinput

maxRed, maxBlue, maxGreen = 12, 14, 13
validIDs = []
for line in fileinput.input(files='adventDay2Input.txt', encoding='utf-8'):

    invalid = False
    # getting game ID
    splitLine = line.split(':')
    idString = splitLine[0]
    gameID = idString[5:]

    # each gameSplit is one bag, three rounds per bag
    line.strip()
    gameSplitLine = line[8:].split(';')

    redCount, blueCount, greenCount = 0, 0, 0
    for round in gameSplitLine:

        # get each colors value
        colorSplit = round.split(',')
        for pull in colorSplit:
            # red count
            if pull.__contains__("red"):
                f = filter(str.isdecimal, pull)
                pull = "".join(f)
                redCount = int(pull)
            # green count
            elif pull.__contains__("green"):
                f = filter(str.isdecimal, pull)
                pull = "".join(f)
                greenCount = int(pull)
            # blue count
            elif pull.__contains__("blue"):
                f = filter(str.isdecimal, pull)
                pull = "".join(f)
                blueCount = int(pull)

        # the game is not valid and we move to the next game id
        if redCount > maxRed or blueCount > maxBlue or greenCount > maxGreen:
            print("invalid ID", gameID)
            invalid = True
            break

    # made it through without finding faults, add to list
    if not invalid:
        validIDs.append(gameID)
        print("valid ID --: ", gameID)
IDSum = 0
for ID in validIDs:
    IDSum += int(ID)

print(IDSum)