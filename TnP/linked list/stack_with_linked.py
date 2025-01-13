class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def create_list(self):
        self.root=None
    
    def insert_left(self,element): 
        n=Node(element)
        if self.root==None:
            self.root=n
        else:
            n.next=self.root
            self.root=n
    
    def delete_left(self):
        if self.root==None:
            print("Empty list")
        else:
            tmp=self.root
            self.root=self.root.next
            print(tmp.data,"deleted")

    def peek(self):
        if self.root==None:
            print("Empty list")
        else:
            print("peek is:",self.root.data)
    
    def print_list(self):
        if self.root==None:
            print("empty")
        else:
            tmp=self.root
            while tmp!=None:
                print(tmp.data,end="--")
                tmp=tmp.next

obj=Node(10)
obj.create_list()
obj.insert_left(10)
obj.insert_left(20)
obj.insert_left(30)
obj.print_list()
print()
obj.delete_left()
obj.print_list()
print()
obj.peek()