birth = list(input())
dayCount = int(input())
max = -1;
maxDay = [];
for i in range(dayCount):
    tempDay = list(input())
    tempNums = [];
    for j in range(8):
        tempNums.append((int(tempDay[j]) - int(birth[j]))**2)
    tempNum = (tempNums[0]+tempNums[1]+tempNums[2]+tempNums[3])*(tempNums[4]+tempNums[5])*(tempNums[6]+tempNums[7])
    if max < tempNum:
        max = tempNum
        maxDay = tempDay
    elif max == tempNum:
        for j in range(8):
            if(maxDay[j] > tempDay[j]):
                max = tempNum
                maxDay = tempDay
                break
            elif(maxDay[j] == tempDay[j]):
                continue
            else:
                break


for i in range(8):
    print(maxDay[i],end="")