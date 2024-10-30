from src.max_depth import max_depth_recursive, max_depth_iterative

def test_max_depth_recursive(root_only, binary_tree):
    """
    Test function for the max_depth_recursive function.
    """
    # Test case 1: Empty list
    assert max_depth_recursive(None) == 0

    # Test case 2: Single node
    assert max_depth_recursive(root_only) == 1

    # Test case 3: Two nodes
    assert max_depth_recursive(binary_tree) == 3


    print("All test cases passed!")

def test_max_depth_iterative(root_only, binary_tree):
    """
    Test function for the max_depth_recursive function.
    """
    # Test case 1: Empty list
    assert max_depth_iterative(None) == 0

    # Test case 2: Single node
    assert max_depth_iterative(root_only) == 1

    # Test case 3: Two nodes
    assert max_depth_iterative(binary_tree) == 3


    print("All test cases passed!")