#print series from start to end in any order
# start:2, end:5,   2,3,4,5
# start:1, end:-3,  1,0,-1,-2,-3

start=int(input("Enter start"))
end=int(input("Enter end"))

if start<end:
    for i in range(start,end+1,+1):
        print(i)

else:
    for i in range (start,end-1,-1):
        print(i)