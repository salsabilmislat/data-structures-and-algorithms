class Node:

   def __init__(self,value):
       self.value=value
       self.next=None


class LinkedList:

    def __init__(self):
        self.head=None

    def insert(self,value):

        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next != None:
                current = current.next
            current.next = node

    def includes(self,value):

        current = self.head

        while current != None:
            if current.value==value:
                return True

            current = current.next

        return False

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

    



if __name__=="__main__":

    newlist=LinkedList()

    newlist.insert(5)
    newlist.insert(8)
    newlist.insert(10)
    newlist.insert(12)
    newlist.insert(4)
    print(newlist)

    if newlist.includes(0):
        print("hi")
    else:
        print("good luck")






