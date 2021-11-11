from code_challenges.stack_and_queue.queue import Node,Queue

import pytest

def test_is_empty():
    """
    Testing is_empty method for a queue
    """
    queue=Queue()
    expected=True
    actual= queue.isEmpty()
    assert expected == actual

def test_enqueue_values():
    """
    Testing enqueue method for a queue
    """
    queue=Queue()
    queue.enqueue(1)
    expected=1
    actual=queue.rear.value

    assert expected == actual


def test_enqueue_multiple_values():
    """
    Testing enqueue method for a queue
    """
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected=3
    actual=queue.rear.value

    assert expected == actual


def test_dequeue_one_value():
    """
    Testing dequeue method for a queue
    """
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(12)
    queue.enqueue(13)
    expected=10
    actual=queue.dequeue()
    assert actual==expected

def test_dequeue_all_value():
    """
    Testing dequeue method for a queue
    """
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    expected=True
    actual=queue.isEmpty()
    assert actual==expected


def test_peek():
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(12)
    queue.enqueue(13)
    expected=10
    actual=queue.peek()
    assert expected==actual

def test_peek_empty_queue():
    queue=Queue()
    expected='This Queue is Empty'
    actual=queue.peek()
    assert expected==actual


