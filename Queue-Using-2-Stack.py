class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                raise IndexError("Queue is empty")
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()


queue = QueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
print(queue.dequeue())  
queue.enqueue(4)
print(queue.dequeue())  
print(queue.dequeue())