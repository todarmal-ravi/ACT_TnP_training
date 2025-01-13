
# def sorting(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
    
# def sorting(arr): #optimised form
#     for i in range(len(arr)-1,-1,-1):
#         for j in range(0,i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

def sorting(arr):#if sorted array is passed then ?
    p=0
    for i in range(0,len(arr)):
        done=True
        for j in range(0,len(arr)-1):
            p+=1
            if arr[j]>arr[j+1]:
                done=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print(p)
        if done ==True:
            break

    print(arr)

lst=[10,20,30,40]
sorting(lst)