#bubble sort

arrayValue = [100,11,2,4,3,4,6]
lengthOfArray = len(arrayValue)

for j in range(0,lengthOfArray-1):
    for i in range(0,lengthOfArray-1-j):
        if(arrayValue[i] > arrayValue[i+1]):
            temp = arrayValue[i]
            arrayValue[i] = arrayValue[i+1]
            arrayValue[i+1] = temp

print(arrayValue)