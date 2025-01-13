
data=[11,22,11,22,44,33,55,66,11]
data1=sorted(set(data))

for i in data1:
    print (f"{i}  {data.count(i)}")