class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, data):
        if self.head is None:
            return False
        elif self.head.data == data:
            self.head = self.head.next
            return True
        else:
            previous_node = self.head
            current_node = self.head.next
            while current_node is not None:
                if current_node.data == data:
                    previous_node.next = current_node.next
                    return True
                previous_node, current_node = current_node, current_node.next
            return False
        
    def show_list(self):
        temp = self.head
        nodes = []
        while(temp):
            nodes.append(str(temp.data))  #wrapped temp.data inside str() because .join() is a string method
            temp = temp.next
        nodes.append('None')
        return ' -> '.join(nodes) 




        

l_list = LinkedList()
l_list.add('a')
l_list.add(4)
l_list.add('c')
print(l_list.show_list())
l_list.remove(4)
print(l_list.show_list())
