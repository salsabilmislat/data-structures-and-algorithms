
from code_challenges.tree_fizz_buzz.tree_fizz_buzz import Node,BinaryTree,breadth_first,fizz_buzz_tree

def test_divisible_by_3():
    tree2=BinaryTree()
    tree2.root=Node(3)
    tree2.root.left=Node(6)
    tree2.root.center=Node(12)
    tree2.root.right=Node(27)
    assert fizz_buzz_tree(breadth_first(tree2))==['Fizz', 'Fizz', 'Fizz', 'Fizz']

def test_divisible_by_5():
    tree2=BinaryTree()
    tree2.root=Node(5)
    tree2.root.left=Node(10)
    tree2.root.center=Node(20)
    tree2.root.right=Node(25)
    assert fizz_buzz_tree(breadth_first(tree2))==['Buzz', 'Buzz', 'Buzz', 'Buzz']

def test_divisible_by_3_and_5():
    tree2=BinaryTree()
    tree2.root=Node(15)
    tree2.root.left=Node(30)

    assert fizz_buzz_tree(breadth_first(tree2))==['FizzBuzz', 'FizzBuzz']


def test_not_divisible_by_3_or_5():
    tree2=BinaryTree()
    tree2.root=Node(1)
    tree2.root.left=Node(17)
    tree2.root.center=Node(14)
    tree2.root.right=Node(2)
    assert fizz_buzz_tree(breadth_first(tree2))==['1', '17', '14', '2']

def test_all_cases():
    tree2=BinaryTree()
    tree2.root=Node(17)
    tree2.root.left=Node(5)
    tree2.root.center=Node(6)
    tree2.root.right=Node(10)
    tree2.root.left.left=Node(12)
    tree2.root.left.right=Node(15)
    tree2.root.right.left=Node(30)
    assert fizz_buzz_tree(breadth_first(tree2))==['17', 'Buzz', 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz', 'FizzBuzz']
