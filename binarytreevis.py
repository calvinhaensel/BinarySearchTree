class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

class BinarySearchTree:
    def __init__(self, contents = []):
        self.root=None


    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value,self.root)


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
        inlist = []
        if root:
	    #First recur on left child
            self.inorder(root.left)
	    #then add the data of node
            inlist.append(root.value)
	    #recur on right child
            self.inorder(root.right) 
        return inlist
     
     
    def postorder(self):
        root = self.root
        postlist = []
        if root:
	    # First recur on left child
            self.postorder(root.left)
	    # the recur on right child
            self.postorder(root.right) 
            postlist.append(root.value)
        return postlist
     
     
    def preorder(self):
        root = self.root
        prelist = []
        if root:
	    # First append node data
            prelist.append(root.value),
	    # Then recur on left child
            self.preorder(root.left)
	    # Finally recur on right child
            self.preorder(root.right)
        return prelist
