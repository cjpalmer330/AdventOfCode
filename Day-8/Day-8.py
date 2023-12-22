import fileinput
from KeyValue import KeyValue

lineNum, leftRight, LRIndex = -1, [], 0
associationDict = {}
# populating dictionary
for association in fileinput.input(files='Day-8-Input.txt', encoding='utf-8'):

    # getting the LR
    if lineNum == -1:
        for character in association:
            leftRight.append(character)

    lineNum += 1
    if lineNum < 2:
        continue
    # adding associations to the dictionary
    keyValuePair = association.split('=')
    keyValue = keyValuePair[0].strip()

    # convert (abc,asd) into [abc,ads]
    pairValue = keyValuePair[1].strip()[1:9]
    valuesArr = pairValue.split(', ')

    # create object
    temp = KeyValue()
    temp.__int__(keyValue, valuesArr[0], valuesArr[1])
    # add objects to dictionary
    associationDict[keyValue] = temp

# looking for ZZZ, starting with AAA
currentElem, numSteps = "AAA", 0
lineNum = 0
print(leftRight)
while currentElem != "ZZZ":

    LorR = leftRight[lineNum % (leftRight.__len__() - 1)]
    print(LorR, lineNum, lineNum % leftRight.__len__())
    if LorR == 'L':
        print(currentElem, " -> ", associationDict.get(currentElem).leftChild)
        currentElem = associationDict.get(currentElem).leftChild
    elif LorR == 'R':
        print(currentElem, " -> ", associationDict.get(currentElem).rightChild)
        currentElem = associationDict.get(currentElem).rightChild
    numSteps += 1
    lineNum += 1

print(numSteps)
print(associationDict.get(currentElem).leftChild)
'''
    
'''
