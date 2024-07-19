def sort(arr):
    sortest = arr[0]
    sortest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < sortest:
            sortest = arr[i]
            sortest_index = arr
        return sortest_index
    
print(sort([1,4,6,3,0,10]))