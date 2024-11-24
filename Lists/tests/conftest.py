import pytest
from src.ListNode import ListNode

@pytest.fixture
def reverse_twice():
    # Creates a sample tree:
    #   1 -> 2 -> 3 -> 4 -> 5 -> 6
    return ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

@pytest.fixture
def reverse_twice_answer():
    # Creates a sample tree:
    #   1 -> 2 -> 3 -> 4 -> 5 -> 6
    return ListNode(3, ListNode(2, ListNode(1, ListNode(6, ListNode(5, ListNode(4))))))
