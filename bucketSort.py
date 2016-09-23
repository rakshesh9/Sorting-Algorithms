import math

def bucketSort(array, n, b, m):

    for i in range(n):
        b[i] = []

    for i in range(n):
        index = math.floor(n * array[i])
        b[index].append(array[i])

    for k in range(n):
        lengthOfArray = len(b[k])
        holdValue = 0

        for i in range(1, lengthOfArray):
            holdValue = b[k][i]
            j = i
            while (j > 0 and b[k][j - 1] > holdValue):
                b[k][j] = b[k][j - 1]
                j = j - 1
                b[k][j] = holdValue
    return b

array = [0.7,0.5,0.1,0.9]
n = len(array)
m = n
b = [i for i in range(n)]
bucketList = bucketSort(array,n,b,m)

outputList = []
for m in bucketList:
    if(len(m) != 0 ):
        for j in m:
            outputList.append(j)
print(outputList)