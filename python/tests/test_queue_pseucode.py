from code_challenges.stack_queue_pseudo.stack_queue_pseudo import Node,Stack,PseudoQueue


import pytest

def test_enqueue():
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    expected=3
    actual=queue.enqueue(3)
    assert expected == actual



def test_dequeue():

    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected=1
    actual=queue.dequeue()
    assert expected == actual



def test_pop_multi_psudo():
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert 1 == queue.dequeue()
    assert 2== queue.dequeue()
    assert 3 == queue.dequeue()


def test_instantiate_an_empty_psuedo():

    with pytest.raises(Exception):
        Pseudo_queue = PseudoQueue()
        Pseudo_queue.dequeue()
