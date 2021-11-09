class Node:

   def __init__(self,value):
       self.value=value
       self.next=None


class LinkedList:

    def __init__(self):
        self.head=None


    def insert(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self,value):

        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next != None:
                current = current.next
            current.next = node

    def __str__(self):

        result = ""

        if self.head is None:
            result += None

        else:
            current = self.head

            while(current):
                result += "{ "+str(current.value)+" } -> "
                current = current.next
            result += "NULL"
            return result



    def zipLists(self, list1,list2):

        list1_curr = list1.head
        list2_curr = list2.head
        while list1_curr != None and list2_curr != None:
            list1_next = list1_curr.next
            list2_next = list2_curr.next
            list1_curr.next = list2_curr
            list2_curr.next = list1_next
            list1_curr = list1_next
            list2_curr = list2_next
            if list1_curr.next == None:
                break
        if list1_curr:
            list1_curr.next = list2_curr

        return list1


if __name__=='__main__':
    list1=LinkedList()
    list2=LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(6)
    list1.append(20)
    list1.append(20)

    list2.append(2)
    list2.append(4)
    list2.append(4)
    list2.append(4)
    list2.append(4)
    list2.append(4)

    list1.zipLists(list1,list2)
    print(list1)








