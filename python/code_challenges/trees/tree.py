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


    ## code challenge 16

    def maximum_value(self):

        if not self.root:

            return "This Tree is Empty"

        self.max=self.root.value

        def traverse(node):

            if node.value>self.max:
                self.max=node.value
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            return self.max

        return traverse(self.root)



class Binary_Search_Tree(BinaryTree):

    def add(self,value):

        node = Node(value)
        if self.root == None:
            self.root = node
            return node.value

        current=self.root
        while current:
            if current.value > value:
                if current.right:
                    current=current.right
                else:
                   current.right=node
                   return

            if current.value < value:
                if current.left:
                    current=current.left
                else:
                   current.left=node
                   return




    def contains(self,value):
        if value == self.root:
            return True
        current=self.root

        while current:
            if current.value > value:
                if current.right:
                    current=current.right
                else:
                    return False

            if current.value < value:
                if current.left:
                    current=current.left
                else:
                    return False
            if current.value == value:
                return True

        return False


if __name__=="__main__":

    tree=BinaryTree()
    tree.root=Node('A')
    tree.root.left=Node('B')
    tree.root.right=Node('C')
    tree.root.left.left=Node('D')
    tree.root.left.right=Node('E')
    tree.root.right.left=Node('F')


    print(tree.pre_order(tree.root))
    print(tree.in_order(tree.root))
    print(tree.post_order(tree.root))

    tree1=Binary_Search_Tree()
    tree1.add("G")
    tree1.add("H")
    tree1.add("I")
    tree1.add("J")

    print(tree1.contains("G"))
    print(tree1.contains("H"))
    print(tree1.contains("I"))
    print(tree1.contains("s"))


   ## code challenge 16

    tree2=BinaryTree()
    tree2.root=Node(1)
    tree2.root.left=Node(5)
    tree2.root.right=Node(10)
    tree2.root.left.left=Node(2)
    tree2.root.left.right=Node(4)
    tree2.root.right.left=Node(3)

    print(tree2.maximum_value())




