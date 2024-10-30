from src.tree_traversals import preOrderTraverseRecursive, inOrderTraverseRecursive, postOrderTraverseRecursive

def test_pre_order_traverse_recursive(sample_tree):
    assert preOrderTraverseRecursive(sample_tree) == [1, 4, 6, 7, 9, 5, 8]

def test_in_order_traverse_recursive(sample_tree):
    assert inOrderTraverseRecursive(sample_tree) == [6, 4, 9, 7, 1, 5, 8]

def test_post_order_traverse_recursive(sample_tree):
    assert postOrderTraverseRecursive(sample_tree) == [6, 9, 7, 4, 8, 5, 1]

def test_in_order_traverse_recursive_binary_tree(binary_tree):
    assert inOrderTraverseRecursive(binary_tree) == [1, 2, 3, 4, 5, 6, 7]
