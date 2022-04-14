

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

'''
Problem: 
https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
'''

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.info, end=' ')
    inOrder(root.right)
    
# def inOrder(root):
    
#     stack = []
    
#     curr = root
    
#     while True:
#         if curr is not None:
#             stack.append(curr)
#             curr = curr.left
#         elif stack:
#             curr = stack.pop()
#             print(curr.info, end=' ')
#             curr = curr.right
#         else:
#             break