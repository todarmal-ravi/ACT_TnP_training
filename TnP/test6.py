# l=[10,20,30,40,50]

# n=int(input("Enter value of n"))

# while n>0:
#     l.append(l[0])
#     l.pop(0)
#     n-=1
#     print(l)



# while n>0:
#     l.insert(0,l[-1])
#     l.pop()
#     n-=1
#     print(l)


#print all number greater than avg of list
l=[33,11,66,22,99,88,44,66,76,34,23,12,56,78]
avg=sum(l)//len(l)
for i in l:
    if i>avg:
        print(i,end=",")