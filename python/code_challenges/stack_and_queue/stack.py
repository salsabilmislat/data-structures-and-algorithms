class Node:

    def __init__(self,value):
       self.value=value
       self.next=None


class Stack:

    def __init__(self):

        self.top=None


    def push(self,value):

        node =Node(value)

        if self.top:
            node.next=self.top

        self.top=node



    def pop(self):

        if self.top != None:

            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value

        else:

            return ('This stack is Empty')


    def peek(self):

        if self.top != None:

            return self.top.value

        else:

            return ('This stack is Empty')

    def isEmpty(self):

        if self.top==None:

            return True

        else:

            return False


