from code_challenges.linked_list_zip.linked_list_zip import LinkedList,Node

import pytest


def test_linked_list_zip_same_len():
    list1=LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2=LinkedList()
    list2.append(4)
    list2.append(5)
    list2.append(6)

    expected = "{ 1 } -> { 4 } -> { 2 } -> { 5 } -> { 3 } -> { 6 } -> NULL"
    list1.zipLists(list1,list2)
    actual = list1.__str__()
    assert expected == actual
