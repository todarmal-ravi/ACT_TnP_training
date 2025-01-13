class Queue:
    def create_Queue(self):
        self.q=[]
        self.front,self.rear=0,-1

    def enqueue(self,element):
        self.rear+=1
        self.q.append(element)
        print(f"{element} inserted on queue")

    
    def dequeue(self):
        if self.front<=self.rear:   
            temp=self.q[self.front]#copy element at front
            self.front+=1
            return temp
        else:
            return "Queue is Empty"
    
    def print_Queue(self):
        #FIFO
        for i in range(self.front,self.rear+1,1):
            print("Queue has:",self.q[i])

queue = Queue()
queue.create_Queue()
while True:
        print("\nStack Operations Menu:")
        print("1. enqueue Element")
        print("2. dequeue Element")
        print("3. Print Stack")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            element = int(input("Enter the element to push: "))
            queue.enqueue(element)
        elif choice == 2:
            print("Element is:",queue.dequeue())
        elif choice == 3:
            queue.print_Queue()
        elif choice == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")