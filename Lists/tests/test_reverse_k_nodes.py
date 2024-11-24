from src.reverse_k_nodes import reverseKGroup


def LinkedListToArray(head):
    """
    Convert a linked list to an array.
    """
    array = []
    current = head
    while current != None:
        array.append(current.val)
        current = current.next
    return array

def test_reverse_k_nodes(reverse_twice):
    """
    Test function for the reverse_k_nodes function.
    """
    # Test case 1:
    # k = 3
    assert LinkedListToArray(reverseKGroup(reverse_twice, 3)) == [3, 2, 1, 6, 5, 4]



    print("All test cases passed!")