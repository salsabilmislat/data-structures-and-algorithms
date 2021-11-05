from code_challenges.linked_list.linked_list import LinkedList,Node

import pytest



def test_empty_linked_list():
    newlist=LinkedList()
    expected = None
    actual = newlist.head
    assert expected == actual

def test_insert_linked_list():
    newlist=LinkedList()
    newlist.insert(10)
    expected = "{ 10 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual

def test_first_node ():
    node = Node(10)
    expected = 10
    actual = node.value
    assert actual == expected

def test_insert_multi_values():
    newlist = LinkedList()
    newlist.insert(10)
    newlist.insert("a")
    expected= "{ 10 } -> { a } -> NULL"
    actual= newlist.__str__()
    assert expected == actual


def test_includes_linked_list(newlist):

    expected=True
    actual=newlist.includes(10)
    assert actual==expected

def test_not_includes_linked_list(newlist):

    expected=False
    actual=newlist.includes(5)
    assert actual==expected

def test_to_string_collection_values(newlist):

    expected= "{ 10 } -> { a } -> { 4 } -> NULL"
    actual= newlist.__str__()

    assert expected==actual

# def test_first_node(newlist):
#     newlist=Node()
#     node = newlist.head
#     expected=10
#     actual = node.value
#     assert expected == actual
#     # assert newlist.head.next.value == 1



@pytest.fixture
def newlist():
    newlist = LinkedList()
    newlist.insert(10)
    newlist.insert("a")
    newlist.insert(4)
    return newlist






