class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '--->'
            itr = itr.next

        print(listr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.get_lastnode()
        listr = ''
        while itr:
            listr += str(itr.data) + '--->'
            itr = itr.prev

        print(listr)

    def get_lastnode(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count


    def insert_at_beginning(self,data):
        if self.head == None:
            self.head=Node(data, self.head, None)
        else:
            self.head.prev=Node(data, self.head, None)
            self.head=Node(data, self.head, None)


if __name__ == '__main__':
    ll=DoublyLinkedList()
    ll.insert_at_beginning(56)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(5)
    ll.print_forward()
    ll.print_backward()
