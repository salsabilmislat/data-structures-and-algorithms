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
    expected= "{ a } -> { 10 } -> NULL"
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

    expected= "{ 4 } -> { a } -> { 10 } -> NULL"
    actual= newlist.__str__()

    assert expected==actual


## the start of code 6


def test_Add_To_End(newlist):

    newlist.append(15)
    expected = "{ 4 } -> { a } -> { 10 } -> { 15 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual

def test_multi_values_to_end(newlist):
    newlist.append(15)
    newlist.append(20)
    expected = "{ 4 } -> { a } -> { 10 } -> { 15 } -> { 20 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual

def test_insert_a_node_before(newlist):
    newlist.insertBefore("a",5)
    expected = "{ 4 } -> { 5 } -> { a } -> { 10 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual


def test_insert_a_node_after(newlist):
    newlist.insertAfter("a",5)
    expected = "{ 4 } -> { a } -> { 5 } -> { 10 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual

def test_node_before_the_first_node(newlist):

    newlist.insertBefore(4,5)
    expected = "{ 5 } -> { 4 } -> { a } -> { 10 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual

def test_after_the_last_node(newlist):
    newlist.insertAfter(10,20)
    expected = "{ 4 } -> { a } -> { 10 } -> { 20 } -> NULL"
    actual = newlist.__str__()
    assert expected == actual

## the start of code 7

def test_greater_than_the_length(newlist):

    expected = 'The K is greater than the length of LinkedList'
    actual = newlist.kthFromEnd(5)
    assert expected == actual

def test_the_length_of_the_list_are_the_same(newlist):
    expected=4
    actual = newlist.kthFromEnd(3)
    assert expected == actual

def test_not_a_positive_integer(newlist):
    expected='The K Must be a positive integer'
    actual = newlist.kthFromEnd(-3)
    assert expected == actual

def test_of_a_size_1():
    newlist = LinkedList()
    newlist.insert(10)
    expected=10
    actual = newlist.kthFromEnd(1)
    assert expected == actual
def test_happy_bath_test_k_is_not_at_end():
    newlist = LinkedList()
    newlist.insert(10)
    newlist.insert('a')
    newlist.insert(4)
    newlist.insert(5)
    newlist.insert(50)
    expected='a'
    actual = newlist.kthFromEnd(1)
    assert expected == actual


@pytest.fixture
def newlist():
    newlist = LinkedList()
    newlist.insert(10)
    newlist.insert("a")
    newlist.insert(4)
    return newlist






