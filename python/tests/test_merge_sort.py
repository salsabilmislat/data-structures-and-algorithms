from code_challenges.merge_sort.merge_sort import merge_sort,merge

def test_mergesort():
    array_sort = [8, 4, 23, 42, 16, 15]
    merge_sort(array_sort)
    actual = array_sort
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_sort_reverse_sorted():
    array_sort = [20, 18, 12, 8, 5, -2]
    merge_sort(array_sort)
    actual = array_sort
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_sort_few_uniques():
    array_sort = [5, 12, 7, 5, 5, 7]
    merge_sort(array_sort)
    actual = array_sort
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sort_nearly_sorted():
    array_sort = [2, 3, 5, 7, 13, 11]
    merge_sort(array_sort)
    actual = array_sort
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
