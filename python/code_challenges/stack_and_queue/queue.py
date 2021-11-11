class Node:

    def __init__(self,value):
       self.value=value
       self.next=None


class Queue:

    def __init__(self):

        self.front=None
        self.rear=None

    def enqueue(self, value):

        node=Node(value)

        if not self.rear:
            self.front=node
            self.rear=node

        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):

        if not self.front:

          raise Exception ('This Queue is Empty')


        temp=self.front
        self.front=self.front.next
        temp.next=None
        return temp.value


    def peek(self):

        if self.isEmpty():

            return ('This Queue is Empty')

        else:
            return self.front.value



    def isEmpty(self):

        return self.front == None
