class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def pprint(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data)+ '--->'
            itr = itr.next

        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data,None)


    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)



    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count


    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1


    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.insert_at_beginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=Node(data,itr.next)

                break
            itr = itr.next
            count+= 1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break

            itr=itr.next

    def remove_after_value(self,data_after):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head = self.head.next
            return

        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=itr.next.next
                break

            itr=itr.next

if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_at_beginning(57)
    ll.insert_at_beginning(8)
    ll.insert_at_end(94)
    ll.insert_values(["saumya","papa","mum"])
    print(ll.get_length())
    ll.insert_after_value("papa","dada")
    ll.remove_after_value("saumya")
    ll.pprint()