
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

    def __str__(self):
        pass

class PseudoQueue:

    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    """
    Add to PseudoQueue class by using the push method from the Stack , using a first-in, first-out approach
    """
    def enqueue(self,value):

        self.stack1.push(value)
        return value


    """
    Add to PseudoQueue class by useing the pop method from the stack , using a first-in, first-out approach
    """
    def dequeue(self):

        if not self.stack1.top:

            raise Exception("empty queue")

        while self.stack1.top:
            stack1_item = self.stack1.pop()
            self.stack2.push(stack1_item)

        item=self.stack2.pop()

        while self.stack2.top:
            stack2_item=self.stack2.pop()
            self.stack1.push(stack2_item)

        return item



if __name__=="__main__":

    newstack=PseudoQueue()

    newstack.enqueue(4)
    newstack.enqueue(2)
    newstack.enqueue(3)

    print(newstack.dequeue())
    print(newstack.dequeue())
    print(newstack.dequeue())
    # print(newstack.dequeue())



    # print(newstack.top.value)
    # newstack.enqueue(10)
    # print(newstack.dequeue())

