cnt = int(input())
numList = []
for i  in range(cnt):
    numList.append(int(input()))
numList.sort()
for num in numList:
    print(num)