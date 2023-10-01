
class Node:

    def __init__(self, key, value) -> None:
        self.left: Node = None 
        self.right: Node = None
        self.height: int = None # The height relative to the bottom of the tree
        self.size: int = None # The amount of nodes in the subtree starting from node
        self.key = key
        self.value = value

        self.updateSizeAndHeight()

    def updateSizeAndHeight(self) -> None:
        self.size = 1
        if self.left != None:
            self.size += self.left.size
        if self.right != None:
            self.size += self.right.size

        self.height = 1
        self.height += max(
            (0 if self.left == None else self.left.height),
            (0 if self.right == None else self.right.height)
        )

    # Returns the balance factor between the left and right subtrees
    def balanceFactor(self) -> int:
        return self.left.height - self.right.height



    # String representation of Node
    def __str__(self) -> str:
        return str(self.key)

    """
    Taken from: https://www.delftstack.com/howto/python/print-binary-tree-python/
    Used for printing out the tree
    """
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
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



""" 
    Used for testing 
"""
def node():

    node = Node(2, 4)
    print(node)

    
if __name__ == "__main__":
    node()

    
    
