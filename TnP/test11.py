#read a line from user and print the largest word

line="this is going to be greatest work"
word_list=line.split()

largest=word_list[0]
length=len(largest)
for word in word_list:

    if len(word)>length:

        length=len(word)
        largest=word

print(largest)


#print largest alphabetically
print(sorted(line.split())[-1])