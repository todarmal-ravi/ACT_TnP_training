
def bst(arr,key):

    start=0
    end=len(arr)

    while start<=end :
        mid=(start+end)//2

        if arr[mid] == key:
            return mid+1
        elif arr[mid]>key :
            end = mid-1
        else :
            start = mid+1
    
    else:
        return -1



lst=[10,20,30,40,50,60,70]
key=int(input("Enter value to be searched:"))

a=bst(lst,key)
if a==-1:
    print("Not Found")
else:
    print(a)
