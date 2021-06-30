a = [11, 3, 58, 31, 56, 77, 43, 12, 65, 19]
d = [90, 0, 8, 34, 1, -9]
c =[0,90,9,-1,34,-9,33444]

def sorting(a):
    for j in range(len(a)):
        for i in range(len(a)-j-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

result = sorting(c)
print(result)
