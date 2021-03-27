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

    def remove(self, node=None, parent=None, left=None):
        """

        :param left:
        :param node:
        :param parent:
        :return:
        """

        if node is None:
            return

        child = node.left or node.right
        if left:
            parent.left = child
        else:
            parent.right = child
        del node


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

def count_children(self):
    return bool(self.left) + bool(self.right)


def is_right_child(self):
    return self.get_parent_and_child_side(self)[1] == \
           "right"


def remove_subtree_minimum(self, subtree):
    """
    supprime le maximum d’un sous-ABR et retourne sa valeur
    :return:maximum
    """
    if subtree is None:
        return
    min_node = subtree.get_min_node()
    minimum = min_node.key
    self.remove(min_node)

    return minimum

def remove_subtree_maximum(self, subtree):
    """
    supprime le maximum d’un sous-ABR et retourne sa valeur
    :return:maximum
    """
    if subtree is None:
        return
    max_node = subtree.get_max_node()
    maximum = max_node.key
    self.remove(max_node)

    return maximum

    def balance_tree(self):
        """
        Équilibre l’arbre courant. Les manipulations de l’arbre ne
        peuvent être faites que via les quatre méthodes de rotations
        ci-dessus durant la procédure sur l’arbre. Elles peuvent donc
        être appelée dans des fonctions appelées par balance_tree.
        Vous ne pouvez pas supprimer et insérer manuellement des
        valeurs (sauf pour la suppression nécessaire dans les
        rotations simple)
        :param self:
        :return: None
        """
        self.display()
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.balance_tree()
        if self.right is None:
            right_size = 0
        else:
            right_size = self.right.balance_tree()
        self.size = 1 + left_size + right_size
        self.balance = self.getBalance()
        self.display()
        while not self.isBalanced():
            if self.balance < 0:

                if self.getSizeOf(self.right.right) < (
                        self.getSizeOf(self.left)
                        +
                        self.getSizeOf(self.right.left)):
                    self.rotate_simple_left()

                else:
                    self.rotate_root_left()

            elif 1 < self.balance:
                if self.getSizeOf(self.left.left) < (
                        self.getSizeOf(self.right)
                        +
                        self.getSizeOf(self.left.right)):
                    self.rotate_simple_right()
                else:
                    self.rotate_root_right()
            self.display()
            print("balance", self.balance)

        if self.isBalanced():
            print("BALANCED")
            return self.size


    def get_max_node(self):
        """

        :return: maximum value node
        """
        maxi = self
        while maxi.right is not None:
            maxi = maxi.right
        return maxi


    def get_min_node(self):
        """

        :return: minimum value node
        """
        mini = self
        while mini.left is not None:
            mini = mini.left
        return mini


    def preOrder(self, node):

        if node is None:
            return

        print(node.key)
        if node.height:
            print("height", node.height)
        self.preOrder(node.left)
        self.preOrder(node.right)
