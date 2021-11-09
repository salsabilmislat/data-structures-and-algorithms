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

    ## the start of code 6


    def append(self,value):

        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next != None:
                current = current.next
            current.next = node


    def insertBefore(self,perValue,valuetoadd):
        newnode=Node(valuetoadd)
        current = self.head
        # if current.value==None:
        #     self.head=newnode

        if self.head.value==perValue:
            newnode.next=self.head
            self.head=newnode


        while current.next != None:
            if current.next.value==perValue:
             newnode=Node(valuetoadd)
             newnode.next=current.next
             current.next=newnode
             return True

            current = current.next
        return False

    def insertAfter(self,nextValue,valuetoadd):
        newnode=Node(valuetoadd)
        current = self.head
        if current==None:
            self.head=newnode

        while current.value != None:
            if current.value==nextValue:
             newnode=Node(valuetoadd)
             newnode.next=current.next
             current.next=newnode
             return True

            if current.value==nextValue and current.next==None:
                current.next=newnode.value
                newnode.next=None


            current = current.next
        return False

    # the start of code 7



    def kthFromEnd(self, k):
            current = self.head
            length = 0
            while current is not None:
                current = current.next
                length += 1

            if k > length:
                print('The K is greater than the length of LinkedList')
                return ('The K is greater than the length of LinkedList')

            if k < 0:
                print('The K Must be a positive integer')
                return ('The K Must be a positive integer')


            current = self.head
            for i in range(0, length - k -1):
                current = current.next


            print(current.value)
            return(current.value)


if __name__=="__main__":

    newlist=LinkedList()
    newlist.insert(4)
    newlist.append(5)
    newlist.append(8)
    newlist.append(10)
    newlist.kthFromEnd(4)
    # newlist.insertBefore(8,6)
    # newlist.insertAfter(10,20)
    print(newlist)

    if newlist.includes(0):
        print("hi")
    else:
        print("good luck")



 # found=False
        # if value.next == None:
        #     return False

        # else:
        #     newNode=Node(valuetoadd)
        #     newNode.next=value.next
        #     value.next=newNode
        # while current:
        #     if current.value==valuetoadd:
        #         prev.next==node
        #         node.next=current
        #         found= True
        #         break

        #     prev=current
        #     current = current.next





