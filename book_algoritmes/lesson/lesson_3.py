def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


def recurs(list):
    if list == []:
        return 0 
    else:
        return 1 + recurs(list[1:])

    
print(recurs([2,4,6]))


def count(list):
    if len(list) == 2:
        return list[0] if list [0] > list[1] else list[1]
    sub_max = count(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(count([2,4,6,355]))

def quicksorted(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [ i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksorted(less) + [pivot] + quicksorted(greater)
    
print(quicksorted([5,2,7,10,323]))


