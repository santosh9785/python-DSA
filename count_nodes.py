class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    
    def insert_end(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    
    def count_nodes(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    
    def search(self, x):
        current = self.head

        while current is not None:
            if current.data == x:
                return "Found"

            current = current.next

        return "Not Found"

    
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


SLL = SinglyLinkedList()

SLL.insert_end(10)
SLL.insert_end(20)
SLL.insert_end(30)

print("Original linked list:")
SLL.display()

print("Total nodes:", SLL.count_nodes())

print("Search for 20:", SLL.search(20))

SLL.reverse()

print("Reversed linked list:")
SLL.display()