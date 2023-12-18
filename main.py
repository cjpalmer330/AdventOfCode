
import fileinput

totalSum = 0
for line in fileinput.input(files='adventDay1Input.txt', encoding='utf-8'):

    # getting line and removing white space
    line = ''.join(line.split())
    tempString = ""

    #each character, if digit add to sum
    for character in line:

        if character.isdigit() and (character != ""):
            tempString += character

    # getting first and last digit
    firstChar = tempString[0]
    tempString = firstChar + tempString[tempString.__len__() - 1]
    totalSum += int(tempString)

print(totalSum)
