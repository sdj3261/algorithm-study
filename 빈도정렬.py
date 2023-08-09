#재귀는 직접 depth 핸드코딩 해보자
def quad(arr,y,x,n) :
    flag = True
    for i in range(y,y+n) :
        for j in range(x,x+n) :
            if arr[y][x] != arr[i][j] :
                flag = False
                break
    if not flag :
        print("(", end = "")
        n = n // 2
        quad(arr,y,x,n)
        quad(arr,y,x+n,n)
        quad(arr,y+n,x,n)
        quad(arr,y+n,x+n,n)
        print(")", end = "")
    elif flag and arr[y][x] == 1:
        print("1", end = "")
    elif flag and arr[y][x] == 0 :
        print("0", end = "")
        

    
        
        
        
                
                


n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n) :
    data = input()
    for j in range(n) :
        arr[i][j] = int(data[j])

quad(arr,0,0,n)


        

    
