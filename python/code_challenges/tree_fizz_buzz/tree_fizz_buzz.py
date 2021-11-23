class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None
        self.center=None



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


class Queue():

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

        if self.rear==self.front:
            temp = self.front
            self.rear =  None
            self.front = None
            return temp.value

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

    queue.enqueue(tree.root)

    ## it can work with front also

    while not queue.isEmpty():
        start=queue.dequeue()
        output.append(start.value)

        if start.left:
            queue.enqueue(start.left)
        if start.center:
            queue.enqueue(start.center)
        if start.right:
            queue.enqueue(start.right)


    return output

def fizz_buzz_tree(k_ary_tree):
    new_k_ary_tree=[]
    for i in k_ary_tree:
        # print(i)

        if i % 3 == 0 and i % 5 == 0:
           new_k_ary_tree.append('FizzBuzz')
        #    print('FizzBuzz')
        elif i %3 == 0:
            new_k_ary_tree.append('Fizz')
            # print('Fizz')
        elif i % 5 == 0:
            new_k_ary_tree.append('Buzz')
            # print('Buzz')
        else:
            new_k_ary_tree.append(str(i))
            # print (str(int(i)))
    return new_k_ary_tree



if __name__=='__main__':

    tree2=BinaryTree()
    tree2.root=Node(17)
    tree2.root.left=Node(5)
    tree2.root.center=Node(6)
    tree2.root.right=Node(10)
    tree2.root.left.left=Node(12)
    tree2.root.left.right=Node(15)
    tree2.root.right.left=Node(30)
    print (breadth_first(tree2))
    # print(type(tree2))
    # print(fizz_buzz_tree(tree2))
    print (fizz_buzz_tree(breadth_first(tree2)))
    # print(fizzBuzz(tree2))








