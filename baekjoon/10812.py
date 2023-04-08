def rotate(array: list, begin: int, end: int, mid: int):
    return array[:begin] + array[mid:end] + array[begin:mid] + array[end:]


i, n = [int(x) for x in input().split()]
array = [i + 1 for i in range(i)]

for _ in range(n):
    i, j, k = [int(x) for x in input().split()]
    array = rotate(array=array, begin=i-1, end=j, mid=k-1)

for v in array:
    print(v, end=' ')