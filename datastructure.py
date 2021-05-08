

def callfunction(arr,d,n):
    for i in range(d):
        arr.append(arr[i])
    for j in range(d):
        arr.remove(arr[0])
    print(arr)


n,d=map(int,input().rstrip().split())

arr=[int(input()) for i in range(n)]


callfunction(arr,d,n)


