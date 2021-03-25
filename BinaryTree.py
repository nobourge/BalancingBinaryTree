# INFO-F103 - Algorithmique - Projet 2
#
# Prénom : Noe
# Nom : Bourgeois
# Matricule : 000496667
"""Nous vous demandons de développer un algorithme qui équilibre un ABR
en utilisant des rotations de racines et simples (droite et gauche)
le plus rapidement possible

Un arbre binaire de recherche est dit équilibré si pour chaque noeud,
la différence entre le nombre de noeud de son sous-arbre gauche et de
son sous-arbre droit vaut 0 ou 1.
Plus formellement, si n est un
noeud d’un arbre T, que T n g est son sous-arbre gauche, T n d son
sous-arbre droit et que |T| est le nombre de noeud de l’arbre T,
l’arbre T est équilibré si : |T n g | −|T n d | ∈ {0,1}, ∀ n ∈ T """

import copy


class BinaryTree:
    def __init__(self, rootVal, leftBinaryTree=None,
                 rightBinaryTree=None):

        self.key = rootVal
        self.left = leftBinaryTree
        self.right = rightBinaryTree

    def getRootVal(self):
        """
        NO MODIFICATION ALLOWED
        :return:
        """
        return self.key

    def setRootVal(self, obj):
        """
        NO MODIFICATION ALLOWED
        :param obj:
        :return:
        """
        self.key = obj

    def getLeftChild(self):
        """
        NO MODIFICATION ALLOWED
        :return:
        """
        return self.left

    def is_left_child(self):
        return self.get_parent_and_child_side(self)[1] == \
               "left"

    def setLeftChild(self, leftChild):
        """
        NO MODIFICATION ALLOWED
        :param leftChild:
        :return:
        """
        self.left = leftChild

    def getRightChild(self):
        """
        NO MODIFICATION ALLOWED
        :return:
        """
        return self.right

    def is_right_child(self):
        return self.get_parent_and_child_side(self)[1] == \
               "right"

    def setRightChild(self, rightChild):
        """
        NO MODIFICATION ALLOWED
        :param rightChild:
        :return:
        """
        self.right = rightChild

    def setSizes(self, node):
        """

        :return:
        """
        if node is None:
            return 0
        node.size = 1 + node.setSizes(node.left) + node.setSizes(
            node.right)
        return node.size

    def getSize(self, node):
        if node is None:
            return 0
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

    def count_children(self):
        return bool(self.left) + bool(self.right)

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

    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left is not None else None
        elif key > self.key:
            return self.right.get(key) if self.right is not None else \
                None
        return self

    def preOrder(self, node):

        if node is None:
            return

        print(node.key)
        if node.height:
            print("height", node.height)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line,
                    second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line,
                    second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (
                n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (
                n - x - 1 + u + y) * ' ' + '\\' + (
                              m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for
                                             a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def get_min_node(self):
        """

        :return: minimum value node
        """
        min = self
        while min.left is not None:
            min = min.left
        return min

    def get_max_node(self):
        """

        :return: maximum value node
        """
        max = self
        while max.right is not None:
            max = max.right
        return max

    def remove(self, node=0, key=None):
        """

        :param node:
        :param key:
        :return:
        """

        if key is not None:
            node = self.get(key)

        if node is None:
            return

        children_count = node.count_children()
        parent, side = self.get_parent_and_child_side(node)

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

    def remove_minimum(self):
        """
        supprime le minimum d’un ABR et retourne sa valeur
        :return:minimum
        """
        if self is None:
            return None
        min_node = self.get_min_node()
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

    def remove_maximum(self):
        """
        supprime le maximum d’un ABR et retourne sa valeur
        :return:maximum
        """
        if self is None:
            return None
        max_node = self.get_max_node()
        maximum = max_node.key
        self.remove(max_node)

        return maximum

    def rotate_root_right(self):
        """
        NO MANUAL VALUE DELETE OR INSERT
        Effectue une rotation de la racine droite sur l’arbre courant ou
         ne modifie pas l’arbre si celle-ci est impossible
        Déplace un ou plusieurs noeuds du sous-arbre gauche vers le
        sous-arbre droit en suivant
        les étapes suivantes :
        — placer b à la racine en conservant
        son sous-arbre gauche d,
        — placer a et son sous-arbre droit c
        comme fils droit de la nouvelle racine b,
        — placer e, l’ancien sous-arbre droit de b, comme fils gauche de a.
        Après cette rotation, b est retiré du sous-arbre gauche et a
        ainsi
        que le sous-arbre e sont rajoutés au sous-arbre droit. Cette
        manipulation est rapide mais le nombre de noeuds transférés
        dépend du nombre de noeuds dans le sous-arbre e.
        :return: None
        """
        if self.left is None:
            return
        previous_root = copy.copy(self)
        new_root = self.left
        previous_root.left = new_root.right
        self = new_root
        self.right = previous_root
        self.setSizes(self)

    def rotate_root_left(self):
        """
        NO MANUAL VALUE DELETE OR INSERT
        Effectue une rotation de la racine gauche sur l’arbre courant
        ou ne modifie pas l’arbre si celle-ci est impossible
        :param self:
        :return: None
        """
        if self.right is None:
            return
        previous_root = copy.copy(self)
        new_root = self.right
        previous_root.right = new_root.left
        self = new_root
        self.left = previous_root
        self.setSizes(self)

    def rotate_simple_right(self):
        """
        Effectue une rotation simple droite sur l’arbre courant ou ne
        modifie pas l’arbre si celle-ci est impossible
        La rotation
        simple droite déplace un noeud du sous-arbre
        gauche vers le sous-arbre droit en suivant les étapes
        suivantes :
        — supprimer le maximum m
        du sous-arbre droit b et l’utiliser comme nouvelle racine,
        — placer a et son sous-arbre droit c comme fils droit de la
        nouvelle racine m,
        — placer b (sans la valeur m) comme fils
        gauche de m.
        Cette rotation est un peu plus longue en terme
        de manipulations, ne permet de transférer qu’un seul noeud
        d’un sous-arbre à l’autre mais le nombre de noeud transféré
        est fixe. Pour pouvoir être effectuées, ces rotations
        requièrent que le racine possède un fils gauche.
        :param self:
        :return: None
        """
        if self.left is None:
            return
        previous_root = copy.copy(self)
        self.key = self.remove_subtree_maximum(self.left)  # not
        # remove_maximum
        # todo find way to find parent with subtree as self
        previous_root.left = None
        self.right = previous_root
        self.setSizes(self)

    def rotate_simple_left(self):
        """
        Effectue une rotation simple gauche sur l’arbre courant ou ne
        modifie pas l’arbre si celle-ci est impossible
        Les
        rotations gauche transferrant des noeuds du sous-arbre droit
        vers le sous-arbre gauche suivent une logique similaire en
        prenant le minimum du sous-arbre droit pour la rotation
        simple gauche
        :return: None
        """
        if self.right is None:
            return
        previous_root = copy.copy(self)
        self.key = self.remove_subtree_minimum(self.right)
        previous_root.right = None
        self.left = previous_root
        self.setSizes(self)

    def getBalance(self, node):
        """
        balance factor must be -1, 0, or 1.
        If the balance factor of a node is
        greater than 1 (left heavy)
        or less than -1 (right heavy), the node needs to be rebalanced
        :param node:
        :return:
        """
        if node is None:
            return 0

        return self.getSize(node.left) - self.getSize(node.right)

    def balance_tree(self):
        """
        Équilibre l’arbre courant. Les manipulations de l’arbre ne
        peuvent être faites que via les quatre méthodes de rotations
        ci-dessus durant la procédure sur l’arbre. Elles peuvent donc
        être appelée dans des fonctions appelées par balance_tree.
        Vous ne pouvez pas supprimer et insérer manuellement des
        valeurs (sauf pour la suppression nécessaire dans les
        rotations simple). Tâchez de combiner les rotations de
        manière à ce que la procédure soit la plus rapide possible
        :param self: :return: None
        """

        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.balance_tree()
        if self.right is None:
            right_size = 0
        else:
            right_size = self.right.balance_tree()
        self.size = 1 + left_size + right_size
        self.balance = self.getBalance(self)

        while (self.balance < -1) or (1 < self.balance):
            if self.balance < -1:
                if self.balance == -2:
                    self.rotate_simple_left()
                else:
                    self.rotate_root_left()

            elif 1 < self.balance:
                if self.balance == 2:
                    self.rotate_simple_right()
                else:
                    self.rotate_root_right()
            self.balance = self.getBalance(self)
            self.display()
            print("balance", self.balance)

        if (-2 < self.balance) and (self.balance < 2):
            self.display()
            print("BALANCED", self.balance)
            return True

    def insert(self, value):
        """
        NO MODIFICATION ALLOWED
        insert value as node as the tree root or the root nearest
        position
        :param value:
        :return:
        """

        if self.getRootVal() is None:
            self.setRootVal(value)
        elif value <= self.getRootVal():
            if self.getLeftChild() is None:
                self.setLeftChild(BinaryTree(value))

            else:
                self.getLeftChild().insert(value)
        else:
            if self.getRightChild() is None:
                self.setRightChild(BinaryTree(value))
            else:
                self.getRightChild().insert(value)

    def init_values(self, values):
        """
        NO MODIFICATION ALLOWED
        :param values:
        :return:
        """
        self.setLeftChild(None)
        self.setRightChild(None)
        self.setRootVal(None)
        self.parent = None
        self.depth = 0
        self.balance = 0
        for v in values:
            self.insert(v)
        self.display()
        # self.height = 1 + self.setDepths(self)
        # self.setHeights(self)
        # self.setDepthsThenHeights(self)
        self.setSizes(self)
