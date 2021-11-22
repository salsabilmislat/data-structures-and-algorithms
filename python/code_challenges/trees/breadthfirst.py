from collections import deque

class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None



class BinaryTree:

    def __init__(self):
        self.root=None

    def pre_order(self, root,output=[]):

        output.append(root.value)
        if root.left is not None:
            self.pre_order(root.left,output)

        if root.right is not None:
            self.pre_order(root.right,output)
        return output

    def in_order(self,root,output=[]):

        if root.left is not None:

            self.in_order(root.left,output)

        output.append(root.value)

        if root.right is not None:

            self.in_order(root.right,output)

        return output

    def post_order(self, root,output=[]):

        if root.left is not None:

            self.in_order(root.left,output)

        if root.right is not None:

            self.in_order(root.right,output)

        output.append(root.value)

        return output


class Node1:

    def __init__(self,value):
       self.value=value
       self.next=None


class Queue(deque):

    def __init__(self):

        self.front=None
        self.rear=None

    def enqueue(self, value):

        node=Node1(value)

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



def breadth_first(tree):
    output=[]
    queue=Queue()

    if tree.root is None:

        return 'this tree is empty'

    queue.append(tree.root)

    while queue:
        start=queue.popleft()
        output.append(start.value)

        if start.left:
            queue.append(start.left)

        if start.right:
            queue.append(start.right)


    return output


if __name__=='__main__':

    tree2=BinaryTree()
    tree2.root=Node(1)
    tree2.root.left=Node(2)
    tree2.root.right=Node(3)
    tree2.root.left.left=Node(4)
    tree2.root.left.right=Node(5)
    tree2.root.right.left=Node(6)

    print(breadth_first(tree2))

