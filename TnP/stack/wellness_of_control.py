class Stack:

    def create_stack(self):
        self.s=[]#size 0
        print(f"Stack created..")

    def push(self,e):
        self.s.append(e)

    def pop(self):
        if len(self.s)>0:
            self.s.pop()
        else:
            print("Stack Empty")

    def is_empty(self):
        return len(self.s)==0


    def print_stack(self):
        for i in range(len(self.s)-1,-1,-1):
            print(self.s[i],end="")


inp=input("Enter a input:")
stack=Stack()
stack.create_stack()
for char in inp:
    if char == '(':
        stack.push(char)
    if char==')':
        if stack.is_empty():
            print("String is False")
            break
        else:
            inp=stack.pop()

else: # will print this statement only if the for loop runs normally, it will not get executed after break        
    print("stack is",stack.is_empty())