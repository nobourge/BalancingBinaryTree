from BinaryTree import BinaryTree

myTree = BinaryTree(None)
root = None

# myTree.init_values(values=[10, 20, 30, 40, 50, 25])

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

myTree.init_values(values=[1, 2, 3])
print("Preorder traversal of the",
      "constructed AVL tree is")
"30 20 10 25 40 50"
myTree.setHeights(myTree)
myTree.preOrder(myTree)
myTree.balance_tree()
myTree.preOrder(myTree)
