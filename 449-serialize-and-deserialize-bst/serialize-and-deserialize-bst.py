# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.serialized = []
        self.index = 0

    def serializeHelper(self, node):
        if not node:
            self.serialized.append("END")
            return

        self.serialized.append(str(node.val))
        self.serializeHelper(node.left)
        self.serializeHelper(node.right)
    
    def deserializeHelper(self, serializedArr):
        if serializedArr[self.index] == "END":
            self.index += 1
            return

        root = TreeNode(int(serializedArr[self.index]))

        self.index += 1

        root.left = self.deserializeHelper(serializedArr)
        root.right = self.deserializeHelper(serializedArr)

        return root

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.serializeHelper(root)
        return ",".join(self.serialized)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.deserializeHelper(data.split(','))
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans