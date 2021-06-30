a = [1, 7, 9, 34, 89, 344]
x = int(input(" Enter the element  : "))

low = 0
high = len(a)-1
mid = 0

def rbinary_searc(a,low,high,x):

    if (low == high):
        if a[low] == x:
            return low
        else:
            return -1
    else:
        mid = (low+high)//2
        if x == a[mid]:
            return mid

        if x <= a[mid]:
            return rbinary_searc(a, low, mid-1, x)
        else:
            return rbinary_searc(a, mid+1, high, x)


result = rbinary_searc(a, low, high, x)

if result != -1:
    print(result)
else:
    print(" does not exist ")
