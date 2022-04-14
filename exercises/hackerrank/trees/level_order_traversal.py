

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque

'''
Problem: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
'''


def levelOrder(root):
    queue = deque()
    
    queue.append(root)
    
    while queue:
        front = queue.popleft()
        print(front.info, end=' ')
        
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)
        
