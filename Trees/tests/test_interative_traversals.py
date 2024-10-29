from src.tree_traversals import preOrderTraverseIterative, inOrderTraverseIterative, postOrderTraverseIterative

def test_pre_order_traverse_iterative(sample_tree):
    assert preOrderTraverseIterative(sample_tree) == [1, 4, 6, 7, 9, 5, 8]

def test_in_order_traverse_iterative(sample_tree):
    assert inOrderTraverseIterative(sample_tree) == [6, 4, 9, 7, 1, 5, 8]

def test_post_order_traverse_iterative(sample_tree):
    assert postOrderTraverseIterative(sample_tree) == [6, 9, 7, 4, 8, 5, 1]

