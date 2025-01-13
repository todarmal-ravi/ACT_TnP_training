#mostly asked 99% 

def Merger(a,start,mid,end):
    i=start
    j=mid+1
    temp=[0]
    temp=temp*len(a)
    #print("temp:",temp)
    ti=start
    while i<=mid and j<=end:
        if a[i]<a[j]:
            temp[ti]=a[i]
            ti+=1
            i+=1
        else:
            temp[ti] = a[j]
            ti+=1
            j+=1

    while i <= mid:
        temp[ti] = a[i]
        ti += 1
        i += 1
        
    while j <= end:
        temp[ti] = a[j]
        ti += 1
        j += 1
    print("temp-",temp)
    for i in range(start,end+1):
        a[i]=temp[i]


def Merge_sort(a,start,end):
    if start<end:
        mid=(start+end)//2
        Merge_sort(a,start,mid)
        Merge_sort(a, mid+1,end)
        Merger(a,start,mid,end)
data=[22,11,77,33,55,44,66,99,88]
#data=[11,22,33,44]
print("Array is:",data)
Merge_sort(data,0,len(data)-1)
print("Array is:",data)