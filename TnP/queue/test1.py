class Queue:
    def create_Queue(self,size):
        self.Maxsize=size
        self.q=[]
        for _ in range(size):
            self.q.append(0)
        self.front,self.rear=0,-1
    def enqueue(self,element):
        self.rear+=1#rear++
        self.q[self.rear]=element
        print(f"{element} inserted on queue")
    def isFull(self):
        if self.rear==self.Maxsize-1:
            return True
        else:
            return False
    def dequeue(self):
        temp=self.q[self.front]#copy element at front
        self.front+=1
        return temp
    def isEmpty(self):
        if self.front>self.rear:
            return True
        else:
            return False
    def print_Queue(self):
        #FIFO
        print("Queue has:",self.q)

queue=Queue()
queue.create_Queue(3)
queue.enqueue(23)
