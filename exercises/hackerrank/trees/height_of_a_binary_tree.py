

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

from collections import deque


'''
    Problem: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
'''



def height(root):
    '''
        BFS Solution
    '''
    queue = deque()
    
    curr = root
    
    curr.level = 0
    queue.append(curr)
    
    curr_level = -1
    
    while queue:
        curr = queue.popleft()
        
        curr_level = curr.level
            
        if curr.left:
            curr.left.level = curr_level + 1
            queue.append(curr.left)

        if curr.right:
            curr.right.level = curr_level + 1
            queue.append(curr.right)
            
    return curr_level


def height(root):
    '''
        DFS Solution
    '''
    if root is None:
        return -1
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    return max([left_height, right_height]) + 1
            
        
