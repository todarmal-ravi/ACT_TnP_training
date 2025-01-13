def sorting(arr):
    
    for i in range(0,len(arr)):
        min=arr[i]
        pos=i

        for j in range(i+1,len(arr)):

            if arr[j]<min :
                min=arr[j]
                pos=j
        
        arr[i],arr[pos]=arr[pos],arr[i]
    
    print(arr)

lst=list(map(int,input("Enter values separated with spaces: ").split()))
sorting(lst)