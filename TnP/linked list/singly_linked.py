class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def create_list(self):
        self.root=None # root is not created but assigned, if the node created is 1st node then it becomes root
    
    def insert_left(self,element): # insert node before current root
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
    
    def print_list(self):
        if self.root==None:
            print("empty")
        else:
            tmp=self.root
            while tmp!=None:
                print(tmp.data,end="--")
                tmp=tmp.next
    
    def insert_right(self,element):
        n=Node(element)
        if self.root==None:
            print("empty")
        else:
            tmp=self.root
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=n
    
    def delete_right(self):
        if self.root==None:
            print("Empty list")
        else:
            tmp=t2=self.root
            while tmp.next!=None:
                t2=tmp
                tmp=tmp.next
            if tmp==self.root:
                self.root=None
            else:
                t2.next=None
            print(tmp.data,"deleted")

    def searching(self,element):
        if self.root==None:
            print("empty")
        else:
            tmp=self.root
            while tmp!=None:
                if tmp.data==element:
                    break
                tmp=tmp.next
            if tmp==None:
                print("Not Found")
            else:
                print("Found")

    def delete_specific(self,element):
        if self.root==None:
            print("empty")
        else:
            tmp=t2=self.root
            while tmp!=None:
                t2=tmp
                if tmp.data==element:
                    break
                tmp=tmp.next
            if tmp==None:
                print("Not Found")
            else:
                if tmp==self.root:
                    self.root=self.root.next #delete left
                elif tmp.next==None:
                    t2.next=None #delete right
                else:
                    t2.next=tmp.next
                print("data deleted:",tmp.data)
        
    def insert_after(self,pos,element):
        if self.root==None:
            print("empty")
        else:
            tmp=self.root
            while tmp!=None:
                if tmp.data==pos:
                    break
                tmp=tmp.next
            if tmp==None:
                print("Not Found")
            else:
                n=Node(element)
                n.next=tmp.next
                tmp.next=n

obj=Node(10)
obj.create_list()
while True:
        print("\nMenu:")
        print("1. Insert Left")
        print("2. Insert Right")
        print("3. Delete Left")
        print("4. Delete Right")
        print("5. Print List")
        print("6. Delete Element")
        print("7. Insert Element After")
        print("8. Search")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at left: "))
            obj.insert_left(data)
        elif choice == 2:
            data = int(input("Enter data to insert at right: "))
            obj.insert_right(data)
        elif choice == 3:
            obj.delete_left()
        elif choice == 4:
            obj.delete_right()
        elif choice == 5:
            obj.print_list()
        elif choice == 6:
            data=int(input("Enter element to be deleted:"))
            obj.delete_specific(data)
        elif choice==7:
            data=int(input("Enter data to be inserted:"))
            pos=int(input("Enter after which element:"))
            obj.insert_after(pos,data)
        elif choice==8:
            data=int(input("Enter data to be searched:"))
            obj.searching(data)
        elif choice==0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")




# # obj.create_list()
# obj.insert_left(10)
# obj.insert_left(20)
# obj.insert_left(30)
# obj.insert_left(40)
# # obj.print_list()
# obj.insert_right(50)
# obj.delete_right()
# obj.insert_after(20,80)
# obj.print_list()


