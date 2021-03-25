def setSizes(self, node):
    """

    :return:
    """
    if node is None:
        return 0
    node.size = 1 + node.setSizes(node.left) + node.setSizes(
        node.right)
    return node.size
