#insertion sort

arrayValue = [100,11,2,4,3,4,6]
lengthOfArray = len(arrayValue)
holdValue = 0

for i in range(1,lengthOfArray):
    holdValue = arrayValue[i]
    j = i
    while(j > 0 and arrayValue[j-1] > holdValue):
        arrayValue[j] = arrayValue[j-1]
        j = j-1
    arrayValue[j] = holdValue    
    
print(arrayValue)