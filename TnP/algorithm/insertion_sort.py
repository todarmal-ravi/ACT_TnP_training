def sorting(arr):
    for i in range(0,len(arr)-1):
        ele=arr[i+1]
        j=i+1
        while j>0 and arr[j-1]>ele :
            arr[j]=arr[j-1]
            j-=1
        arr[j]=ele
    print(arr)

lst=list(map(int,input("Enter elements separated with space: ").split()))
sorting(lst)