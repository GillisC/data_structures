from bst import BST
from node import Node
import random

class AVL(BST):
    
    def _putHelper(self, node: Node, key, value: int) -> Node:
        node = super()._putHelper(node, key, value)

        balanceFactor = self._heightHelper(node.left) - self._heightHelper(node.right)
        
        if balanceFactor > 1:
            if self._heightHelper(node.left.left) - self._heightHelper(node.left.right) > 0:
                return self._rightRotate(node)
            else:
                node.left = self._leftRotate(node.left)
                return self._rightRotate(node)
        elif balanceFactor < -1:
            if self._heightHelper(node.right.right) - self._heightHelper(node.right.left) > 0:
                return self._leftRotate(node)
            else:
                node.right = self._rightRotate(node.right)
                return self._leftRotate(node)
            
        return node

    
    def _rightRotate(self, parent: Node):
        child: Node = parent.left

        assert child, "There must be a left child"

        temp: Node = child.right
        child.right = parent
        parent.left = temp

        parent.updateSizeAndHeight()
        child.updateSizeAndHeight()

        return child
    
    def _leftRotate(self, parent: Node):
        child: Node = parent.right

        assert child, "There must be a right child"

        temp: Node = child.left
        child.left = parent
        parent.right = temp

        parent.updateSizeAndHeight()
        child.updateSizeAndHeight()

        return child


""" Used for testing """
def main():
    avl = AVL()

    for _ in range(0, 100):
        avl.put(random.randint(50, 150), 1)

    print("Binary Search Tree:")
    avl.display()
    print("\n")
    

    



if __name__ == "__main__":
    main()