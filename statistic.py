import math
import copy

arr = [72.2,31.9,26.5,29.1,27.3,8.6,22.3,26.5,20.4,12.8,25.1,19.2,24.1,58.2,68.1,89.2,55.1,9.4,14.5,13.9,20.7,17.9,8.5,55.4,38.1,54.2,21.5,26.2,59.1,43.3]
arr.sort()
sarr = []
def mean(arr):
    mean = sum(arr)/float(len(arr))
    return mean
    
def median():
    if(len(arr) %2 != 0):
        med = arr[len(arr)-1//2]
    else:
        med = (arr[len(arr)//2]+arr[(len(arr)-1)//2])/2
    print("sample median: ", med)
    return med

def frequency(start,period,end):
    for  k in range(start,end,period):
        print(k,"to",k+period,":")
        sarr=[]
        for i in arr:
            if(i<=k+period and k <= i ):
                sarr.append(i)
        print("frequency",len(sarr))
        print(sarr)

def trimMean10(arr):
    tempArr = copy.deepcopy(arr)
    del tempArr[-3:]
    del tempArr[:3]
    return(mean(tempArr))


print("arr: ",arr)
print("len: ",len(arr))
print("mean: ",mean(arr));
print("trimmedMean 10%:",trimMean10(arr));

