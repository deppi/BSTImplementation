#!/usr/bin/python2.7
import random

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.value = val
    def print_node():
        print str(root.left) + " " + str(root.value) + "(" + str(root.parent) + ")" + " " + str(root.right)

class BST:
    def __init__(self):
        self.top = None # top refers to top of the tree
                # makes a new BST with empty root

    def __init__(self, node):
        self.top = node # makes a new BST with node as the root
        self.top.parent = None # top level has no parent

    def print_bst(self):
        self.print_bst_wrapped(self.top, "")

    def print_bst_wrapped(self, n, depth):
        if n is None:
            return
        self.print_bst_wrapped(n.right, depth + "-")
        print depth + str(n.value) + "(" + str(n.parent) + ")"
        self.print_bst_wrapped(n.left, depth + "-")

    def insert(self, node):
        if type(node) is int: # allows user to just pass an int
            n = Node(node)
            return self.insert_wrapped(self.top, n)
        return self.insert_wrapped(self.top, node)

    def insert_wrapped(self, root, node):
        if root is None:
            self.top = node
            return
        if node.value > root.value:
            if (root.right is not None): 
                return self.insert_wrapped(root.right, node)
            else:
                root.right = node
                node.parent = root # keep a reference to the parent
                return
        else:
            if (root.left is not None):
                return self.insert_wrapped(root.left, node)
            else:
                root.left = node
                node.parent = root # keep a reference to the parent
                return

    def search(self, value):
        return self.search_wrapped(self.top, value)

    def search_wrapped(self, root, value):
        if root is None:
            return False
        if root.value == value:
            return True
        elif value > root.value:
            return self.search_wrapped(root.right, value)
        else:
            return self.search_wrapped(root.left, value)

    def find_predecessor(self):
        return self.find_predecessor_wrapped(self.top)

    def find_predecessor_wrapped(self, root): # finds predecessor ROOTED AT 'root'
        if root.left is None: # this node has no predecessor
            return None
        root = root.left # go left once
        while (root.right is not None): # then go right as much as possible
            root = root.right
        return root

    def find_successor(self):
        return self.find_successor_wrapped(self.top)

    def find_successor_wrapped(self, root): # finds successor ROOTED AT 'root'
        if root.right is None: # this node has no successor
            return None
        root = root.right # go right once
        while (root.left is not None): # then go left as much as possible
            root = root.left
        return root
    
    def delete(self, value):
        self.delete_wrapped(self.top, value)

    def delete_wrapped(self, root, value): # pre-condition: a BST. post-condition: a BST with 'value' removed
        if root is None: # nothing to delete
            return
        if value == root.value: # deleting the root
            if (root.left is not None):
                predecessor = self.find_predecessor_wrapped(root) # get the predecessor
                root.value = predecessor.value # swap the values
                return self.delete_wrapped(root.left, predecessor.value)
            if (root.right is not None):
                successor = self.find_successor_wrapped(root) # get the successor
                root.value = successor.value # swap the values
                return self.delete_wrapped(root.right, successor.value)
            else:
                # cant just say root = None
                if (self.top.value == root.value): # if we are deleting the root 
                    self.top = None
                elif (root.parent.left is not None and root.value == root.parent.left.value): # other cases
                    root.parent.left = None
                else:
                    root.parent.right = None
        elif value > root.value:
            if root.right is not None:
                if root.right.value == value: # found the value to be deleted on the right
                    if root.right.right is None and root.right.left is None: # node to be deleted is a leaf
                        root.right = None # forget about the value
                        return
                    elif root.right.right is None and root.right.left is not None: # node to be deleted has a only left
                        root.right = root.right.left
                        return
                    elif root.right.right is not None and root.right.left is None: # node to be deleted has a only right
                        root.right = root.right.right
                        return
                    else: # node to be deleted has a left and a right
                        # this is confusing unless you draw it out and label your nodes.
                        successor = self.find_successor_wrapped(root.right) # get the successor
                        root.right.value = successor.value # swap the values
                        return self.delete_wrapped(root.right.right, successor.value)
                else:
                    return self.delete_wrapped(root.right, value) # haven't found the value but know it's on the right
            else: 
                return # value is not in tree
        elif value < root.value:
            if root.left is not None:
                if root.left.value == value: # found the value to be deleted on the left
                    if root.left.right is None and root.left.left is None: # node to be deleted is a leaf
                        root.left = None # forget about the value
                    elif root.left.right is None and root.left.left is not None: # node to be deleted has only a left
                        root.left = root.left.left
                        return
                    elif root.left.right is not None and root.left.left is None: # node to be deleted has only a right
                        root.left = root.left.right
                        return
                    else: # node to be deleted has a left and a right
                        # this is confusing unless you draw it out and label your nodes.
                        predecessor = self.find_predecessor_wrapped(root.left) # get the predecessor
                        root.left.value = predecessor.value # swap the values
                        return self.delete_wrapped(root.left.left, predecessor.value)
                else:
                    return self.delete_wrapped(root.left, value) # haven't found the value but know it's on the left
            else:
                return # value is not in tree
        else:
            return # value is not in tree


t = BST(Node(500))
#for i in range(0, 50):
#        t.insert(Node(random.randint(0,999)))

t.insert(10)
t.insert(5)
t.insert(7)
t.insert(1)
t.insert(0)
t.insert(9)
t.insert(50)
t.insert(25)
t.insert(15)
t.insert(30)
t.insert(100)
t.insert(110)
t.insert(75)
t.insert(90)
t.insert(80)
t.insert(95)
t.insert(85)
t.insert(92)
t.insert(99)
t.insert(70)

t.print_bst()

t.delete(75)

t.print_bst()
