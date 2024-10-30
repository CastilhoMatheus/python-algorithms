import pytest
from src.TreeNode import TreeNode

@pytest.fixture
def sample_tree():
    # Creates a sample tree:
    #        1
    #       / \
    #      4   5
    #     / \   \
    #    6   7   8
    #       /
    #      9
    return TreeNode(1, TreeNode(4, TreeNode(6), TreeNode(7, TreeNode(9))), TreeNode(5, None, TreeNode(8)))

@pytest.fixture
def binary_tree():
    #         4
    #       /   \
    #      2     6
    #     / \   / \
    #    1   3 5   7

    return TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))

@pytest.fixture
def root_only():

    return TreeNode(1)