
class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
	
    def __iter__(self):
        if self.left != None:
            for elem in self.left:
                yield elem
		
        yield self.value
	
        if self.right != None:
            for elem in self.right:
                yield elem    

class BinarySearchTree:
    def __init__(self, contents = []):
        self.root=None
        for item in contents:
            self.insert(item)
	    
    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])    


    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value,self.root)
        return self


    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left==None:
                cur_node.left=Node(value)
                cur_node.left.parent=cur_node
            else:
                self._insert(value,cur_node.left)
        elif value>cur_node.value:
            if cur_node.right==None:
                cur_node.right=Node(value)
                cur_node.right.parent=cur_node
            else:
                self._insert(value,cur_node.right)
        else:
                print("Value already in tree!")	    

    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)


    def delete(self,value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node==None or self.find(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None 	
        def min_value_node(n):
            current=n
            while current.left!=None:
                current=current.left
            return current
        def num_children(n):
            num_children=0
            if n.left!=None: 
                num_children+=1
            if n.right!=None: 
                num_children+=1
            return num_children
        node_parent = node.parent
        node_children = num_children(node)
	#Case 1
        if node_children == 0:
            if node_parent!=None:
                if node_parent.left==node:
                    node_parent.left=None
                else:
                    node_parent.right=None
        else:
            self.root = None
	#Case 2
        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right	
            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else: 
                self.root = child	
            child.parent = node_parent
	#Case 3
        if node_children == 2:
            new = min_value_node(node.right_child)
            node.value = new.value
            self.delete_node(new)
	    
    def contains(self, value):
        if self.root != None:
            return self._contains(value, self.root)
        else:
            return False

    def _contains(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self._contains(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._contains(value, cur_node.right)
        return False
	
	

    def inorder(self):
        root = self.root
        inlist, curr = [], root
        while curr:
            if curr.left is None:
                inlist.append(curr.value)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    inlist.append(curr.value)
                    node.right = None
                    curr = curr.right
        return inlist
     
     
    def postorder(self):
        postlist,root = [], self.root
        self._postorder(root, postlist)
        return postlist
    #Added a helper function to do the required recursion
    def _postorder(self, node, plist):
        if node == None:
            return
        self._postorder(node.left, plist)
        self._postorder(node.right, plist)
        plist.append(node.value)
        
     
     
    def preorder(self):
        root = self.root
        if not root:
            return []
        prelist,curr = [],root
        while curr:
            if curr.left is None:
                prelist.append(curr.value)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right 
                if node.right is None:
                    prelist.append(curr.value)
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right            
        return prelist
    
    def levelorder(self):
        root = self.root
        if root is None:
            return []
        levellist, current = [], [root]
        while current:
            next_level = []
            for node in current:
                levellist.append(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
        return levellist    
