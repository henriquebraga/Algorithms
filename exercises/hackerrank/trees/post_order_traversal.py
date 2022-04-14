

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

'''
Problem: 
https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?isFullScreen=true
'''

def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    
    print(root.info, end=' ')
