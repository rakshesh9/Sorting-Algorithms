#merge sort

#divide the array
def MergeSort(array):
    
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        MergeSort(left)
        MergeSort(right)
        Merge(array,left,right)


#merge two sorted array
def Merge(array,left,right):
        
        i=0
        j=0
        k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k]=left[i]
                i=i+1
            else:
                array[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            array[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            array[k]=right[j]
            j=j+1
            k=k+1

#example,chage any array and it will work
array = [40,3,7,21,1,5]
MergeSort(array)
print(array)