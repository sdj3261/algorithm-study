data =  [8,5,7,9,2,10]

def insertionSort(data):
    for i in range(1,len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and data[j] > key :
            data[j+1] = data[j]
            j-=1
        data[j+1] = key

def binarySort(data, target) :
    l = 0
    r = len(data)-1
    cnt = 0

    while l<=r :
        mid = (l+r)//2
        if target == data[mid] :
            return mid
        elif target < data[mid] :
            r = mid - 1
        else :
            l = mid+1
        cnt += 1
    return -1
insertionSort(data)
print(binarySort(data, 9))
print(data)