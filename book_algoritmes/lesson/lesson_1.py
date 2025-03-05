def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
#my_list = [1, 3, 5, 7, 9]
#print(binary_search(my_list, 3))
#print(binary_search(my_list, -1))



def findSmaller(arr):
    smaller = arr[0]
    smaller_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i 
        return smaller_index
def SelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smaller = findSmaller(arr) # type: ignore
        newArr.append(arr.pop(smaller))
    return newArr