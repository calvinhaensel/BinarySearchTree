class Node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None

class binary_search_tree:
    def __init__(self):
        self.root=None


    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)


    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
                cur_node.left_child.parent=cur_node
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
                cur_node.right_child.parent=cur_node
            else:
                self._insert(value,cur_node.right_child)
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
            while current.left_child!=None:
                current=current.left_child
            return current
        def num_children(n):
            num_children=0
            if n.left_child!=None: 
                num_children+=1
            if n.right_child!=None: 
                num_children+=1
            return num_children
        node_parent = node.parent
        node_children = num_children(node)
	#Case 1
	


def inorder(root):
    inlist = []
    if root:
        #First recur on left child
        inorder(root.left)
        #then add the data of node
        inlist.append(root.val)
        #recur on right child
        inorder(root.right) 
 
 
def postorder(root):
    postlist = []
    if root:
        # First recur on left child
        postorder(root.left)
        # the recur on right child
        postorder(root.right) 
        postlist.append(root.val)
 
 
def preorder(root):
    prelist = []
    if root:
        # First append node data
        prelist.append(root.val),
        # Then recur on left child
        preorder(root.left)
        # Finally recur on right child
        preorder(root.right)
