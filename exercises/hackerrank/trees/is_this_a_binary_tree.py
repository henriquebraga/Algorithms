""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

from collections import deque, namedtuple


def check_binary_search_tree_(root):
    '''
        Recursive solution.
    '''
    def is_valid_bst(node, lower, upper):
        if node is None:
            return True

        if not (lower < node.data < upper):
            return False

        return is_valid_bst(
            node=node.left,
            lower=lower,
            upper=node.data
        ) and is_valid_bst(
            node=node.right,
            lower=node.data,
            upper=upper
        )

    return is_valid_bst(
        node=root,
        lower=float('-inf'),
        upper=float('inf')
    )
    

    rom collections import deque, namedtuple


Boundary = namedtuple('Boundary', 'node lower upper')


def check_binary_search_tree_(root):
    '''
        BFS solution
    '''
    
    queue = deque()
    
    queue.append(
        Boundary(root, float('-inf'), float('inf'))
    )
    
    while queue:
        element = queue.popleft()
        
        if element.node:
            if not (element.lower < element.node.data < element.upper):
                return False
            
            queue.append(
                Boundary(
                    element.node.left,
                    element.lower,
                    element.node.data
                )
            )

            queue.append(
                Boundary(
                    element.node.right,
                    element.node.data,
                    element.upper
                )
            )
            
    return True