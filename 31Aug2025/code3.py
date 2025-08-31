class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_data, data):
        curr = self.head
        while curr and curr.data != prev_data:
            curr = curr.next
        if not curr:
            return
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    def delete(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            return
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print(elems)

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    ll.insert_after(1, 1.5)
    ll.display()
    print("Length:", ll.length())
    print("Search 2:", ll.search(2))
    ll.delete(1.5)
    ll.display()
    ll.reverse()
    ll.display()