# part 1 input
trialTimes = [34908986]
prevRecord = [204171312101780]
waysToBeatRecord = [0, 0]

# part 2 input
# trialTimes = [34908986]
# prevRecord = [204171312101780]
index, doesntWork = 0, 0

for trial in trialTimes:

    trialNum, wayToBeat = 0, 0
    while trialNum < trial:
        remainingTime = trial - trialNum
        # for second run on 7, the remaining time is 5, and the trial num is 5. 5 seconds at 2mm/s
        distance = remainingTime * trialNum
        if distance > prevRecord[index]:
            wayToBeat += 1
        elif trialNum > doesntWork:
            doesntWork = trialNum
        trialNum += 1
        print(trialNum)



    waysToBeatRecord[index] = wayToBeat
    index += 1
print(waysToBeatRecord)