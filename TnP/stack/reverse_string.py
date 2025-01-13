class Stack:
    def create_stack(self):
        self.string=[]#size 0
        print(f"Stack created..")

    def push(self,word):
        for i in word:
            self.string.append(i)

    def print_stack(self):
        for i in range(len(self.string)-1,-1,-1):
            print(self.string[i],end="")


stack = Stack()
word=input("Enter string:")
stack.create_stack()
stack.push(word)
stack.print_stack()


