import fileinput

points, lineNum, totalMatching = 0, 0, 0
for drawLine in fileinput.input(files='adventDay4Input.txt', encoding='utf-8'):

    numberOfMatching = 0

    # getting winning numbers
    splitLine = drawLine.split('|')
    idString = splitLine[0]
    winningNumbers = idString[10:]
    winningNumbersArr = winningNumbers.strip().split(' ')

    # all numbers drawn
    drawnNums = splitLine[1]
    drawnNumsArr = drawnNums.strip().split(' ')

    # checking for winning numbers
    for drawn in drawnNumsArr:

        if not drawn.isnumeric():
            continue
        for winner in winningNumbersArr:
            if not winner.isnumeric():
                continue
            if drawn == winner and drawn is not (" " or "" or "\n" or "\t"):
                numberOfMatching += 1

    # calculating points
    if numberOfMatching > 0:
        tempPoints = 2 ** (numberOfMatching - 1)
        print(numberOfMatching, tempPoints, points)
        points += tempPoints
        totalMatching += numberOfMatching
    lineNum += 1
    print(lineNum)

print(points)
print(totalMatching)
