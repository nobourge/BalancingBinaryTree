from BinaryTree import BinaryTree
import random


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


values = set()
for _ in range(5):
      values.add(random.randint(0, 9))


myTree.init_values(values)
myTree.balance_tree()
# myTree.preOrder(myTree)
myTree.display()
print("balance:", myTree.balance)
