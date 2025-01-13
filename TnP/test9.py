
# reverse a line word by word
line = "this is test line"
word_list = line.split()[::-1] #gives words

new_line=""
for i in word_list:
    new_line+=i+" "

print(new_line)