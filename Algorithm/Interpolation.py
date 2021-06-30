import math
array = [1, 2, 3, 4, 5, 7]
target = int(input(" Enter a number  : "))

def intepolation(array,target):
    start = 0
    end = len(array)-1

    while start< end and target >= array[start] and target <= array[end]:

        pos = int(start + ((end - start) / (array[end] - array[start]) * (target - array[start])))
        if array[pos] == target:
            return pos

        if target > array[pos]:
            start = pos+1

        elif target < array[pos]:
            end = pos-1

    return " Not Found "

result = intepolation(array, target)
print(result)
