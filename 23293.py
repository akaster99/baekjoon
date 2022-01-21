logCount, playerCount = input().split(" ");
logCount = int(logCount)
playerCount = int(playerCount)

itemList = [[0 for i in range(54)] for j in range(playerCount+1)]
areaList = [1 for i in range(playerCount+1)]
logList = [];
banPlayer = set();

for logNumber in range(1,logCount+1):
    log = input().split(" ");
    log[0] = int(log[0])#로그번호
    log[1] = int(log[1])#player번호
    log[3] = int(log[3])#상호작용 번호
    
    if(log[2] == 'A'):
        if(areaList[log[1]] != areaList[log[3]]):
            banPlayer.add(log[1]);
            logList.append(log[0]);
    elif(log[2] == 'F'):
        if(areaList[log[1]] != log[3]):
            logList.append(log[0])
        itemList[log[1]][log[3]] += 1
    elif(log[2]=='C'):
        log[4] = int(log[4])
        if((itemList[log[1]][log[3]] > 0) and (itemList[log[1]][log[4]] > 0) ):
            itemList[log[1]][log[3]] -= 1
            itemList[log[1]][log[4]] -= 1
        else:
            logList.append(log[0])

    else:
        areaList[log[1]] = log[3]


print(len(logList))
for t in logList:
    print(t, end=" ")
if(len(logList) != 0):
    print()
print(len(banPlayer))
for t in banPlayer:
    print(t, end=" ")