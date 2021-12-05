from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort():
    array_sort = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(array_sort)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_sort_reverse_sorted():
    array_sort = [20, 18, 12, 8, 5, -2]
    actual = insertion_sort(array_sort)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_sort_few_uniques():
    array_sort = [5, 12, 7, 5, 5, 7]
    actual = insertion_sort(array_sort)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sort_nearly_sorted():
    array_sort = [2, 3, 5, 7, 13, 11]
    actual = insertion_sort(array_sort)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_empty_array():
    array_sort = []
    actual = insertion_sort(array_sort)
    expected = 'this array is empty'
    assert actual == expected
