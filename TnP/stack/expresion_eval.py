class Stack:
    def create_stack(self):
        self.s=[]#size 0
        self.top=-1
        self.ans=0
        print(f"Stack created..")

    def push(self,e):
        self.s.append(e)
        self.top+=1
        print()
        # print("Element pushed")

    def pop(self):
        if len(self.s)>0:
            self.top-=1
            print(self.s.pop(),end="")
        else:
            print("Stack Empty")

    def is_empty(self):
        return len(self.s)==0

    def peek(self):
        if len(self.s)>0:
            print("Element at peek:",self.s[-1])
        else:
            print("Stack Empty")


    def print_stack(self):
        for i in range(len(self.s)-1,-1,-1):
            print(self.s[i],end=" ")

    def operation(self,ch):
        a=self.s[self.top]
        self.s.pop()
        # print(self.top)
        b=self.s[self.top]
        self.s.pop()
        # print(a)
        # print(b)

        if ch == '+':
            self.ans+=a+b
        if ch == '-':
            self.ans+=a-b
        if ch == '*':
            self.ans+=a*b
        if ch == '/':
            self.ans+=a / b
        if ch == '%':
            self.ans+=a % b

        stack.push(self.ans)


list1=input("Enter a input:").split()
stack=Stack()
stack.create_stack()

for ch in list1:
    if ch.isdigit()==True:
        stack.push(int(ch))
        stack.print_stack()
    else:

        stack.operation(ch)

# print(ans)