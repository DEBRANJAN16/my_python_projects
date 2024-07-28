class BST:
    
    def __init__(self, val, left=None,right=None):
        
        self.val = val
        self.left = left
        self.right = right
        
    def add(self, root, data):
        
        if root is None:
            return "Insertion failed, Empty root"
        return self.addHelper(root, data)
    
    def addHelper(self, root, data):
        
        if root is None:
            return BST(data)
        
        if data < root.val:
            if root.left is None:
                root.left = BST(data)
                
            else:
                self.addHelper(root.left,data)
                
        elif data > root.val:
            if root.right is None:
                root.right = BST(data)
            else:
                self.addHelper(root.right, data)
        else:
            return "insertion failed: duplicate value"
        
        return "insertion completed"

    def remove(self, root, data):
        if root is None:
            return "deletion failed: deleting from an empty tree"
        return self.removeHelper(root, data)

    def removeHelper(self, root, data):
        if root is None:
            return root, "deletion failed: could not find value"

        if data < root.val:
            root.left, message = self.removeHelper(root.left, data)
        elif data > root.val:
            root.right, message = self.removeHelper(root.right, data)
        else:
            if root.left is None:
                return root.right, "deletion completed"
            elif root.right is None:
                return root.left, "deletion completed"

            temp = self.findMin(root.right)
            root.val = temp.val
            root.right, message = self.removeHelper(root.right, temp.val)
        
        return root, "deletion completed"

    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorderTraversal(self, root):
        elements = []
        self.inorderHelper(root, elements)
        return elements

    def inorderHelper(self, node, elements):
        if node:
            self.inorderHelper(node.left, elements)
            elements.append(node.val)
            self.inorderHelper(node.right, elements)
            
# Example usage
root = BST(10)
root.add(root, 5)
root.add(root, 15)
root.add(root, 2)
root.add(root, 7)
root.add(root, 12)
root.add(root, 20)

print(root.inorderTraversal(root)) 

root.remove(root, 15)
print(root.inorderTraversal(root)) 
        
        