def mergeSort(arr):
    L=R=[]
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

    i = j = k = 0
    #while len(L) > i  and len(R) > j :
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # We ran out of elements either in L or R
    # so we will go through the remaining elements and add them
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end ="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end ="\n")
    printList(arr)