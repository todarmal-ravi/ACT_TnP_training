class Stack:
    def create_stack(self):
        self.s=[]#size 0
        print(f"Stack created..")

    def push(self,e):
        self.s.append(e)
        print("Element pushed")

    def pop(self):
        if len(self.s)>0:
            print("Element poped:",self.s.pop())
        else:
            print("Stack Empty")

    def peek(self):
        if len(self.s)>0:
            print("Element at peek:",self.s[-1])
        else:
            print("Stack Empty")


    def print_stack(self):
        for i in range(len(self.s)-1,-1,-1):
            print(self.s[i])

            
stack = Stack()
stack.create_stack()
while True:
        print("\nStack Operations Menu:")
        print("1. Push Element")
        print("2. Pop Element")
        print("3. Peek Element")
        print("4. Print Stack")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            element = int(input("Enter the element to push: "))
            stack.push(element)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.print_stack()
        elif choice == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


