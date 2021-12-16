class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data, self.head)
        self.head=node

    def pprint(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listr=''
        while itr:
            listr += str(itr.data)+ '--->'
            itr=itr.next


if __name__ == '__main__':
    pass