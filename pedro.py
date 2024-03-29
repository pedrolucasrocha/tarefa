class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

    def peek(self):
        if self.is_empty():
            return
        return self.front.data

    def display_queue(self):
        node = self.front
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()

# Testando o código
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display_queue()  # Deve exibir: 1 2 3

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.display_queue()  # Deve exibir: 1 2 3 4 5 6

q.dequeue()
q.dequeue()
q.display_queue()  # Deve exibir: 3 4 5 6

print("Primeiro elemento:", q.peek())  # Deve exibir: Primeiro elemento: 3

if q.is_empty():
    print("Fila está vazia")
else:
    print("Fila não está vazia")  # Deve exibir: Fila não está vazia
