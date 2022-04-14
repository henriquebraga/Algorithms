

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

'''
Problem: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
'''


    def insert(self, val):
        node = Node(val)
        
        if not self.root:
            self.root = node
            return self.root
        
        curr = self.root
        
        while True:
            if curr.left is None and val <= curr.info:
                curr.left = node
                break
            if curr.right is None and val > curr.info:
                curr.right = node
                break
                
            if val <= curr.info:
                curr = curr.left
            else:
                curr = curr.right
        return self.root
                
                
        
        
        #Enter you code here.

