def partition (arr, low, high):
    # the partition's job is to place the pivot between smaller and larger values
    pivot = arr[high]
    i = (low - 1) # keeping track of the small values

    for j in range(low , high):

        if arr[j] <= pivot:
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1




def quicksort (arr, low , high ):
    # select a pivot, move all values less than the pivot to the left and greater than to the right
    # repeat for each partition
    if low < high:

        pi = partition(arr, low , high)

        quicksort(arr , low , pi - 1)
        quicksort(arr , pi + 1, high)

if __name__ == "__main__":
    unsortedList = [2 ,7, 3,8 ,24 ,16,9]
    # unsortedList.sort()
    # print unsortedList
    quicksort(unsortedList , 0 , len(unsortedList) -1 )
    print unsortedList
