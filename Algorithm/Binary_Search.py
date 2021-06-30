#a = [1, 34, 7, 89, 9, 344]
a = [3, 6, 8, 12, 14, 17, 90]
target = int(input(" Element : "))

def binary_search(a,target):
    right = len(a) - 1
    left = 0

    while left <= right:

        mid = (right+left)//2

        if target == a[mid]:
            return mid

        elif target < a[mid]:
            right = mid-1

        else:
            left = mid+1


result = binary_search(a, target)

print(result)
