from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.tree_intersection.tree import Node,BinaryTree
from code_challenges.tree_intersection.hash_map import HashTable

def test_tree_intersection():
    tree_one = BinaryTree()
    tree_one.root = Node(150)
    tree_one.root.left = Node(100)
    tree_one.root.right = Node(250)

    tree_two = BinaryTree()
    tree_two.root = Node(42)
    tree_two.root.left = Node(100)
    tree_two.root.right = Node(600)

    actual = tree_intersection(tree_one, tree_two)
    expected = [100]
    assert actual == expected



def test_tree_intersection_trees_empty():
    tree_one = BinaryTree()
    tree_two = BinaryTree()
    tree_two.root = Node(42)
    tree_two.root.left = Node(100)
    tree_two.root.right = Node(600)

    actual = tree_intersection(tree_one, tree_two)
    expected = "there is no repeat"
    assert actual == expected


def test_tree_no_intersection():
    tree_one = BinaryTree()
    tree_one.root = Node(150)
    tree_one.root.left = Node(100)
    tree_one.root.right = Node(250)
    tree_one.root.left.left = Node(75)


    tree_two = BinaryTree()
    tree_two.root = Node(42)
    tree_two.root.left = Node(101)
    tree_two.root.right = Node(600)
    tree_two.root.left.left = Node(15)

    actual = tree_intersection(tree_one, tree_two)
    expected = "there is no repeat"
    assert actual == expected

