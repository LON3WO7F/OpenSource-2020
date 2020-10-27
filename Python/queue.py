# Simple queue Data Structure
class Queue:

    def __init__(self):
        self.data = []

    #Check if Queue is empty
    def is_empty(self):
        return len(self.data) == 0

    #Add element to the queue
    def enqueue(self, value): # insert
        self.data.insert(0, value)

    #Delete element from the queue
    def dequeue(self): # delete
        if self.is_empty():
            return "Cannot delete from empty queue"
        return self.data.pop()

    #Get size of the queue
    def size(self):
        return len(self.data)

    #Display the contents of the queue
    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            print("Contents: ", end='')
            for i in range(len(self.data)): # printing from rear to front
                print(self.data[i], end=' ')
        print()

# #Test
# q1 = Queue()
# print(q1.is_empty()) #Check if queue is empty
# q1.enqueue(1)
# q1.enqueue(2)
# q1.display()
# q1.dequeue()
# q1.display()
# print(q1.is_empty()) #Check if queue is empty