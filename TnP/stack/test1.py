class stack:
    def create_stack(self,size):
        self.maxSize=size
        self.top=-1
        self.s=[] # create empty list without size

        for i in range(0,size,1):
            self.s.append(0) #create empty stack with size
    
    def push(self,value):
        if self.isFull()==False:
            self.top+=1
            self.s[self.top]=value
        else:
            print("Stack Full")

    def pop(self):
        if self.isEmpty() == False:
            tmp=self.s[self.top]
            self.top-=1
            print("element popped:",tmp)
        else:
            print("empty")

    
    def isFull(self):
        if self.top==(self.maxSize-1):
            return True
        else:
            return False
        
    def peek(self):
        if self.isEmpty()!=True:#if not full
            print("Element poped:",self.s[self.top])
        else:
            print("Stack Empty")
        
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    
    def print_stack(self):
        for i in range(self.top,-1,-1):
            print(self.s[i])

obj=stack()


size=int(input("Enter size:"))
obj.create_stack(size)

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Print")
    print("5. Exit")
    choice=int(input("Enter Choice:"))
    if choice==1:
        ele=int(input("enter element to push:"))
        obj.push(ele)
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.peek()
    elif choice==4:
        obj.print_stack()
    elif choice==5:
        print("Thanks")
        break
    else:
        print("Enter valid input")
