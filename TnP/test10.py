line="this is a test line for training"
a=line.count('a')

vowels="aeiou"
sum=0
for i in vowels:
    print(i,"-",line.count(i))
    sum+=line.count(i)
print(sum)