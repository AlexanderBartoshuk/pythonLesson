import random


class MapAlgo:


    def invoke(nums: [int], target:int) -> [int]:
        result = []
        map = {int: int}  # key: int - значения элемента списка, value - индекс элемента списка с этим значением
        steps = 0 # итерации цикла

        for i, num in enumerate(nums):
            looking_value = target - num  # 7

            if looking_value in map:
                result = [i, map[looking_value]]
            else:
                map[num] = i
                steps += 1
                print("MapAlgo steps:", steps)

        return result

class LoopAlgo:

    def invoke(nums: [int], target:int) -> [int]:
        result = []
        steps = 0

        for i in range(0, nums.__len__() - 1):
            for j in range(i + 1, nums.__len__()):
                if (nums[i] + nums[j] == target):
                    result = [i, j]
                    return result

                steps += 1
                print("LoopAlgo steps:", steps)

        return []


list = []

for i in range(0, 1000000):
    list.append(random.randint(-1_000_000, 1_000_000))
target = random.randint(-1_000_000, 1_000_000)

input("Press enter to start MapAlgo")

result = MapAlgo.invoke(list, target)
print("MapAlgo Result =", result)


input("Press enter to start LoopAlgo")

result = LoopAlgo.invoke(list, target)
print("LoopAlgo Result =", result)