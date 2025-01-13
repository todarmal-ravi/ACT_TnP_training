# implement sliding window to print max of each window given that size of window is 3


q=[5,10,8,3,6,2,9]
size=int(input("Enter size:"))
for start in range(0,len(q)-size + 1,1):
    print(q[start:(size+start)],"  ",max(q[start:(size+start)]))