class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None



class BinaryTree:

    def __init__(self):
        self.root=None

    def post_order(self):

        output = []
        if not self.root :
            return 'Empty Tree'

        def traverse(root):
            if root.left :
                traverse(root.left)

            if root.right :
                traverse(root.right)

            output.append(root.value)

        traverse(self.root)
        return output




