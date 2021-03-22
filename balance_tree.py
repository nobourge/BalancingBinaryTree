from BinaryTree import BinaryTree

myTree = BinaryTree(None)
root = None

myTree.init_values(values=[10, 20, 30, 40, 50, 25])

"""The constructed abr
            10
              \
               20
                 \
                 30
                /  \
               25   40
                     \
                     50
AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""

# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
"30 20 10 25 40 50"
myTree.preOrder(myTree)
myTree.remove_maximum()
myTree.preOrder(myTree)
