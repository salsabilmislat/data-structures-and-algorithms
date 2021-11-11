from code_challenges.stack_and_queue.stack import Node,Stack


import pytest


def test_is_empty():
    """
    Testing is_empty method for a Stack
    """
    stack=Stack()
    expected=True
    actual= stack.isEmpty()
    assert expected == actual

def test_push():
    """
    Testing push method for a Stack
    """
    stack=Stack()
    stack.push(3)
    expected=3
    actual=stack.top.value

    assert expected == actual

def test_push_multiple_values():
    """
    Testing push method for a Stack
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    expected=3
    actual=stack.top.value

    assert expected == actual

def test_multiple_pops():
    """
    Testing pop method for a Stack
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    expected=True
    actual=stack.isEmpty()
    assert actual==expected

def test_pop():
    """
    Testing pop method for a Stack
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    expected=3
    actual=stack.pop()
    assert actual==expected
    
def test_peek():
    """
    Testing peek method for a Stack
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    expected=3
    actual=stack.peek()
    assert expected==actual

def test_peek_empty_stack():
    stack=Stack()
    expected='This stack is Empty'
    actual=stack.peek()
    assert expected==actual

