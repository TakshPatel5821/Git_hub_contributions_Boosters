# algorithms.py
from typing import List, Optional

def sort_algorithm(arr: List[int]) -> List[int]:
    """Sort with even numbers first, then odd numbers (or similar ordering by parity then value)."""
    return sorted(arr, key=lambda x: (x % 2, x))

def calculate_mean(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def calculate_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def reverse_string(s: str) -> str:
    return s[::-1]

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    r = int(num**0.5) + 1
    for i in range(3, r, 2):
        if num % i == 0:
            return False
    return True

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values: List[int]) -> Optional[Node]:
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head
