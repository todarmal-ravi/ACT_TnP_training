#implement binary search tree using list


def insert(tree,data,i):
    
    if tree[0]==-1:
        tree[0]=data
    else:
        if data<tree[i]:
            if tree[2*i+1]==-1:
                tree[2*i+1]=data
            else:
                insert(tree,data,2*i+1)
        
        else:
            if tree[2*i+2]==-1:
                tree[2*i+2]=data
            else:
                insert(tree,data,2*i+2)

def search(tree,key,i):

    if tree[0]==-1:
        print("Empty Tree")
    else:
        if key<tree[i]:
            if tree[2*i+1]==-1:
                print("Not Found")
            else:
                search(tree,key,2*i+1)
        
        else:
            if tree[2*i+2]==-1:
                print("Not Found")
            else:
                search(tree,key,2*i+2)

size=int(input("Enter size:"))

tree=[]

for _ in range(0,size*2):
    tree.append(-1)

while True:
    element=int(input("Enter value to be inserted(-1 for end):"))
    if element==-1:
        break
    insert(tree,element,0)
print(tree)