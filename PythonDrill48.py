# Python drill for step 48
#
# Python Version: 3.6.0
#
# Author: Terry Soltz
#
# Purpose: To develop a sorting algorithm


# Define mergeSort using three parameters: list, starting index, ending index

def mergeSort(myList):
    subMergeSort(myList, 0, len(myList) - 1)
    
def subMergeSort(myList, first, last):
    mid = first + (last - first) // 2
    if first < last: # list segment has more than one element
        
        # Call mergeSort on each half
        subMergeSort(myList, first, mid)
        subMergeSort(myList, mid + 1, last)

    # Merge halves
    i = first
    j = mid + 1
    k = 0
    tmp = [None] * (last - first + 1)
    while i <= mid and j <= last:
        if myList[i] < myList[j]:
            tmp[k] = myList[i]
            i += 1
        else :
            tmp[k] = myList[j]
            j += 1
        k += 1
        
    while i <= mid:
        tmp[k] = myList[i]
        i += 1
        k += 1
    while j <= last:
        tmp[k] = myList[j]
        j += 1
        k += 1
    k = 0
    for i in range(first, last + 1):
        myList[i] = tmp[k]
        k += 1

# Define lists and sort

testList1 = [67, 45, 2, 13, 1, 998]
mergeSort(testList1)
print(testList1)

testList2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
mergeSort(testList2)
print(testList2)


