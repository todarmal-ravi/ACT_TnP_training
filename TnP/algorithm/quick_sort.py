# most asked

def quick_sort(arr,start,end):
    i=start
    j=end
    pivot=start
    while i<j:
        while arr[i]<arr[pivot]:
                i+=1
        while arr[j]>arr[pivot]:
                j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if i<end:
        quick_sort(arr,i+1,end)
    if j>start:
        quick_sort(arr, start,j-1)