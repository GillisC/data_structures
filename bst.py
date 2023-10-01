from node import Node
from typing import Iterator
import random


class BST:

    root: Node # The BST root node

    def __init__(self) -> None:
        self.root = None

    
    def getSize(self):
        return self._sizeHelper(self.root)

    def _sizeHelper(self, node: Node):
        if node == None:
            return 0
        return node.size
    
    def getHeight(self):
        return self._heightHelper(self.root)

    def _heightHelper(self, node: Node):
        if node == None:
            return 0
        return node.height
    
    """Returns the value of the node with the same key, or creates a new node if no node exist with the given key"""
    def get(self, key) -> int:
        value: int = self.getHelper(self.root, key)
        return value
    
    """Uses recursion to go down the BST"""
    def _getHelper(self, key, node: Node) -> int:
        if node == None:
            value = 0
            self.put(key, value)
            return value
    
        if key < node.key:
            return self._getHelper(key, node.left)
        elif key > node.key:
            return self._getHelper(key, node.right)
        return node.value
    
    """Adds a new node to the BST"""
    def put(self, key, value: int):
        if key == None:
            raise("No key")
        
        self.root = self._putHelper(self.root, key, value)

    def _putHelper(self, node: Node, key, value: int) -> Node:
        if node == None:
            return Node(key, value)

        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self._putHelper(node.left, key, value)
        elif key > node.key:
            node.right = self._putHelper(node.right, key, value)
        
        node.updateSizeAndHeight()
        return node


    def __iter__(self) -> Iterator[int]:
        yield from self._iterHelper(self.root)

    def _iterHelper(self, node: Node):
        if node is not None:
            yield from self._iterHelper(node.left)
            yield node
            yield from self._iterHelper(node.right)

    def display(self):
        lines, *_ = self.root._display_aux()
        for line in lines:
            print(line)


""" Used for testing """
def main():
    bst = BST()
    avl = AVL()

    for _ in range(0, 100):
        bst.put(random.randint(50, 150), 1)
        avl.put(random.randint(50, 150), 1)

    print("Binary Search Tree:")
    bst.display()
    print("\n")

    print("Same tree but balanced:")
    avl.display()
    

    



if __name__ == "__main__":
    main()