from code_challenges.trees.breadthfirst import Node,BinaryTree,Node1,Queue,breadth_first

import pytest

def test_breadth_first():
    tree2=BinaryTree()
    tree2.root=Node(1)
    tree2.root.left=Node(2)
    tree2.root.right=Node(3)
    tree2.root.left.left=Node(4)
    tree2.root.left.right=Node(5)
    tree2.root.right.left=Node(6)
    assert breadth_first(tree2)==[1, 2, 3, 4, 5, 6]


def test_empty_breadth_first():
    tree2=BinaryTree()
    assert breadth_first(tree2)=='this tree is empty'
