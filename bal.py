def setSizes(self, node):
    """

    :return:
    """
    if node is None:
        return 0
    node.size = 1 + node.setSizes(node.left) + node.setSizes(
        node.right)
    return node.size


def setDepths(self, node, depth=0, max_depth=0):
    """

    :return: None
    """
    if node is None:
        return max_depth
    node.depth = depth
    if max_depth < depth:
        max_depth = depth

    max_depth = self.setDepths(node.left, depth + 1, max_depth)
    if max_depth < depth:
        max_depth = depth
    max_depth = self.setDepths(node.right, depth + 1, max_depth)

    return max_depth


def setDepthsThenHeights(self, node, depth=0, max_depth=0):
    """

    :return: None
    """
    if node is None:
        return max_depth
    node.depth = depth
    if max_depth < depth:
        max_depth = depth

    max_depth = self.setDepthsThenHeights(node.left, depth + 1,
                                          max_depth)

    max_depth = self.setDepthsThenHeights(node.right, depth + 1,
                                          max_depth)
    node.height = 1 + max_depth - depth
    return max_depth


def getDepth(self):
    return self.depth


def setHeights(self, node, height=-1):
    """

    :return: None
    """
    if node is None:
        return
    if height == -1:
        height = self.height
    node.height = height
    self.setHeights(node.left, height - 1)
    self.setHeights(node.right, height - 1)


def getHeight(self, node):
    if not node:
        return 0
    return node.height

def get_parent_and_child_side(self, node, current=None):
    """
    :return:
    """
    if current is None:
        current = self
    parent, side = None, None
    if node is None:  # or (node.left is None and node.right is
        # None):
        return
    if current.left is not None:
        left_child_key = current.left.key
        if current.left == node:
            parent, side = (current, "left")
            return parent, side

    if current.right is not None:
        right_child_key = current.right.key
        if current.right == node:
            parent, side = (current, "right")
            return parent, side

    if current.left is not None:
        parent, side = self.get_parent_and_child_side(node,
                                                      current.left)
    if current.right is not None:
        parent, side = self.get_parent_and_child_side(node,
                                                      current.right)

    return parent, side


def remove(self, node=None, parent=None, side=None):
    """

    :param side:
    :param node:
    :param parent:
    :return:
    """

    if node is None:
        return

    children_count = node.count_children()

    if children_count == 0:

        if side == "left":
            parent.left = None
        else:
            parent.right = None
        del node

    elif children_count == 1:
        child = node.left or node.right
        if side == "left":
            parent.left = child
            del node
        elif side == "right":
            parent.right = child
            del node
        else:
            root = node
            root.key = child.key
            root.left = child.left
            root.right = child.right
            del child

    else:
        successor = node.get_successor()
        node.key = successor.key
        successor_parent, side = self.get_parent_and_child_side(
            successor)
        if side == "left":
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
        del successor


def get_successor(self):
    if self.right is not None:
        return self.right.min()
    node = self
    while node.is_right_child():
        node = self.get_parent_and_child_side(node)[1]
    return self.get_parent_and_child_side(node)[1]  # is
    # None
    # if not node.is_left_child() so
    # no successor

def is_right_child(self):
    return self.get_parent_and_child_side(self)[1] == \
           "right"
