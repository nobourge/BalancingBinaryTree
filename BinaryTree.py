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


class BinaryTree:
    def __init__(self, rootVal, leftBinaryTree=None,
                 rightBinaryTree=None):
        self.parent = None
        self.height = 1
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

    def count_children(self):
        return bool(self.left) + bool(self.right)

    def get_parent_and_child_side(self, node, current=None):
        """
        works if every node key is unique
        :return:
        """
        if current is None:
            current = self
        parent, side = None, None
        if node is None:    # or (node.left is None and node.right is
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

    def get_min_node(self):
        min = self
        while min.left is not None:
            min = min.left
        return min

    def get_max_node(self):
        max = self
        while max.right is not None:
            max = max.right
        return max

    def remove(self, node=0, key=None):

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
                node.parent.right = child
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

    def remove_subtree_maximum(self, key):
        """
        supprime le maximum d’un sous-ABR et retourne sa valeur
        :return:maximum
        """
        node = self.get(key)
        if node is None:
            return
        next = node.right
        while next.right is not None:
            next = next.right
        maximum = next.key
        self.remove(next)
        return maximum

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
        La rotation de la racine droite déplace un ou plusieurs noeuds du sous-arbre gauche vers
        le sous-arbre droit tel qu’illustré sur la Figure 2 en suivant les étapes suivantes :
        — placer b à la racine en conservant son sous-arbre gauche d,
        — placer a et son sous-arbre droit c comme fils droit de la nouvelle racine b,
        — placer e, l’ancien sous-arbre droit de b, comme fils gauche de a.
        Après cette rotation, b est retiré du sous-arbre gauche et a ainsi que le sous-arbre e sont
        rajoutés au sous-arbre droit. Cette manipulation est rapide mais le nombre de noeuds
        transférés dépend du nombre de noeuds dans le sous-arbre e.
        :return: None
        """

    def rotate_root_left(self):
        """
        NO MANUAL VALUE DELETE OR INSERT
        Effectue une rotation de la racine gauche sur l’arbre courant
        ou ne modifie pas l’arbre si celle-ci est impossible
        :param self:
        :return: None
        """

    def rotate_simple_right(self):
        """
        Effectue une rotation simple droite sur l’arbre courant ou ne
        modifie pas l’arbre si celle-ci est impossible
        La rotation simple droite déplace exactement un noeud du sous-arbre gauche vers le
        sous-arbre droit tel qu’illustré sur la Figure 3 en suivant les étapes suivantes :
        — supprimer le maximum m du sous-arbre droit b et l’utiliser comme nouvelle racine,
        — placer a et son sous-arbre droit c comme fils droit de la nouvelle racine m,
        — placer b (sans la valeur m) comme fils gauche de m.
        Cette rotation est un peu plus longue en terme de manipulations, ne permet de transférer
        qu’un seul noeud d’un sous-arbre à l’autre mais le nombre de noeud transféré est fixe.
        Pour pouvoir être effectuées, ces rotations requièrent que le racine possède un fils gauche. Les
        rotations gauche transferrant des noeuds du sous-arbre droit vers le sous-arbre gauche suivent
        une logique similaire en prenant le minimum du sous-arbre droit pour la rotation simple gauche
        :param self:
        :return: None
        """
        if self.left is None:
            return
        previous_root = self
        self.key = self.left.remove_maximum()
        previous_root.left = None
        self.right = previous_root
        self.setHeights(self)

    def rotate_simple_left(self):
        """
        Effectue une rotation simple gauche sur l’arbre courant ou ne
        modifie pas l’arbre si celle-ci est impossible
        :return: None
        """
        if self.right is None:
            return
        previous_root = self
        self.key = self.right.remove_minimum()
        previous_root.right = None
        self.left = previous_root
        self.setHeights(self)

    def setHeights(self, node, height=1):
        """

        :return: None
        """
        if node is None:
            return
        node.height = height
        self.setHeights(node.left, height + 1)
        self.setHeights(node.right, height + 1)

    def getHeight(self, node):
        if not node:
            return 0

        return node.height

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

        return self.getHeight(node.left) - self.getHeight(node.right)

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
        self.setHeights(self)
        balance = self.getBalance(self)
        print("balance", balance)
        if (-2 < balance) and (balance < 2):
            return self

        elif balance < -1:
            self.rotate_simple_left()

        elif 1 < balance:
            self.rotate_simple_right()

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
        for v in values:
            self.insert(v)
