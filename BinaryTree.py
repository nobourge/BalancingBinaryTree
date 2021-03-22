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
        return self.get_parent_and_child_side(self.key)[1] == "left"

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
        return self.get_parent_and_child_side(self.key)[1] == "right"

    def setRightChild(self, rightChild):
        """
        NO MODIFICATION ALLOWED
        :param rightChild:
        :return:
        """
        self.right = rightChild

    def count_children(self):
        return bool(self.left) + bool(self.right)

    def get_parent_and_child_side(self, node):
        """
        works if every node key is unique
        :param key:
        :return:
        """

        if node is None or (node.right is None and node.left is None):
            return
        if node.left is not None:
            left_child_key = node.left.key
            if left_child_key == key:
                return node, "left"

        if node.right is not None:
            right_child_key = node.right.key
            if right_child_key == key:
                return (node, "right")

        if node.left is not None:
            parent, side =  node.left.get_parent_and_child_side(key)
        if node.right is not None:
            parent, side =  node.right.get_parent_and_child_side(key)

        return parent, side

    def get_successor(self):
        if self.right is not None:
            return self.right.min()
        node = self
        while node.is_right_child():
            node = self.get_parent_and_child_side(node.key)[1]
        return self.get_parent_and_child_side(node.key)[1]  # is None
        # if not node.is_left_child() so
        # no successor

    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left is not None else None
        elif key > self.key:
            return self.right.get(key) if self.right is not None else\
                None
        return self

    def preOrder(self, node):

        if not node:
            return

        print(node.key)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def min(self):
        node = self
        while node.left is not None:
            node = node.left
        return node

    def max(self):
        node = self
        while node.right is not None:
            node = node.right
        return node

    def remove(self, node=0, key=None):

        if key is not None:
            node = self.get(key)

        if node is None:
            return

        children_count = node.count_children()
        parent, side = self.get_parent_and_child_side(node.key)

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
                    successor.key)
            if side == "left":
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            del successor

    def remove_maximum_subtree(self, key):
        """
        supprime le maximum d’un ABR et retourne sa valeur
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

    def remove_maximum(self):
        """
        supprime le maximum d’un ABR et retourne sa valeur
        :return:maximum
        """
        if self is None:
            return None

        if self.right is None:
            max_node = self
        else:
            next_node = self.right
            while next_node.right is not None:
                next_node = next_node.right
            max_node = next_node
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
        else:
            tmp = self
            self.key = self.left.remove_maximum()


    def rotate_simple_left(self):
        """
        Effectue une rotation simple gauche sur l’arbre courant ou ne
        modifie pas l’arbre si celle-ci est impossible
        :return: None
        """
        if self.left is None:
            return
        else:
            tmp = self

    def getHeight(self, node):
        if not node:
            return 0

        return node.height

    def getBalance(self, node):
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
                # self.left.parent = self  # todo delete
                # self.left.height = self.height + 1  # todo delete

            else:
                self.getLeftChild().insert(value)
        else:
            if self.getRightChild() is None:
                self.setRightChild(BinaryTree(value))
                # self.right.parent = self  # todo delete
                # self.right.height = self.height + 1  # todo delete
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
