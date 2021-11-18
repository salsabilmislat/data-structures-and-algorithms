from code_challenges.trees.tree import Node,BinaryTree,Binary_Search_Tree

import pytest


def test_empty_tree():

    # with pytest.raises(Exception):
    #     tree=Binary_Search_Tree()
    #     tree.add()
    with pytest.raises(Exception):
        tree=BinaryTree()
        tree.root.value

def test_single_root_node():

    # tree1=Binary_Search_Tree()
    # assert tree1.add("G")=="G"
    tree=BinaryTree()
    tree.root=Node('A')
    assert tree.root.value=='A'

def test_add_a_left_child_and_right_child():

    tree1=Binary_Search_Tree()
    tree1.add("G")
    tree1.add("H")
    tree1.add("I")

    assert tree1.contains("G")==True
    assert tree1.contains("H")==True
    assert tree1.contains("I")==True


def test_preorder():
    tree=BinaryTree()
    tree.root=Node('A')
    tree.root.left=Node('B')
    tree.root.right=Node('C')
    tree.root.left.left=Node('D')
    tree.root.left.right=Node('E')
    tree.root.right.left=Node('F')
    assert tree.pre_order(tree.root)==['A', 'B', 'D', 'E', 'C', 'F']


def test_inorder():
    tree=BinaryTree()
    tree.root=Node('A')
    tree.root.left=Node('B')
    tree.root.right=Node('C')
    tree.root.left.left=Node('D')
    tree.root.left.right=Node('E')
    tree.root.right.left=Node('F')
    assert tree.in_order(tree.root)==['D', 'B', 'E', 'A', 'F', 'C']


def test_postorder():
    tree=BinaryTree()
    tree.root=Node('A')
    tree.root.left=Node('B')
    tree.root.right=Node('C')
    tree.root.left.left=Node('D')
    tree.root.left.right=Node('E')
    tree.root.right.left=Node('F')
    assert tree.post_order(tree.root)==['D', 'B', 'E', 'F', 'C', 'A']
