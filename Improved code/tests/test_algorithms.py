
import pytest
from algorithms import (
    sort_algorithm, calculate_mean, calculate_fibonacci,
    reverse_string, is_prime, binary_search, create_linked_list
)

def test_sort_algorithm():
    assert sort_algorithm([3,1,4,2,5]) == [4,2,1,3,5]

def test_calculate_mean():
    assert calculate_mean([1,2,3,4]) == 2.5
    assert calculate_mean([]) is None

def test_fibonacci():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(5) == 5

def test_reverse_string():
    assert reverse_string("abc") == "cba"

def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(15)

def test_binary_search():
    arr = [1,3,5,7,9]
    assert binary_search(arr, 5) == 2
    assert binary_search(arr, 2) == -1

def test_create_linked_list():
    head = create_linked_list([1,2,3])
    values = []
    cur = head
    while cur:
        values.append(cur.value)
        cur = cur.next
    assert values == [1,2,3]
