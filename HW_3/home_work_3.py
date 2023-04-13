class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def add_to_start(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def reverse_linked_list(self, tail = None):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next_node



linked_list = LinkedList()
linked_list.add_to_start(9)
linked_list.add_to_start(5)
linked_list.add_to_start(1)
linked_list.add_to_end(201)
linked_list.add_to_end(204)

print("Исходный связанный список")
linked_list.print_list()
linked_list.reverse_linked_list()
print("\nРазвернутый связанный список")
linked_list.print_list()

