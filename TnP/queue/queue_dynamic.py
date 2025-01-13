class Queue:
    def create_Queue(self):
        self.q=[]

    def enqueue(self,element):
        self.q.append(element)
        print(f"{element} inserted on queue")


    def dequeue(self):
        temp=self.q.pop(0)
        return temp

    def isEmpty(self):
        if len(self.q)==0:
            return True
        else:
            return False

    def print_Queue(self):
        #FIFO
        print(self.q)

queue = Queue()
queue.create_Queue()
while True:
        print("\nQueue Operations Menu:")
        print("1. Enqueue Element")
        print("2. Dequeue Element")
        print("3. Print Queue")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter the element: "))
            queue.enqueue(element)

        elif choice == 2:
            if queue.isEmpty()!=True:
                print("Element dequeued:",queue.dequeue())
            else:
                print("Queue Empty")

        elif choice == 3:
            if queue.isEmpty()!=True:
                print("Queue has")
                queue.print_Queue()
            else:
                print("Queue Empty")

        elif choice==0:
            print("Thanks for using the code ...")
            break
        else:
            print("Invalid choice! Please try again.")

