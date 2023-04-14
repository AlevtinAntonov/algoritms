#!/usr/bin/python

class NilNode(object):
    """
    The nil class is specifically for balancing a tree by giving all  traditional leaf noes tw children that are null
     and waiting to be filled
    """
    def __init__(self):
        self.red = False


NIL = NilNode() # Nil is the sentinel value for nodes


class RBNode(object):
    """
    Class for implementing the nodes that the tree will use
    For self.color:
        red == False
        black == True
        If the node is a leaf it will either
    """
    def __init__(self,data):
        self.red = False
        self.parent = None
        self.data = data
        self.left = NIL
        self.right = NIL

class RedBlackTree(object):
    """
    Class for implementing a standard red-black trees
    """
    def __init__(self):
        self.root = None
        self.size =0
    def add(self,data,curr = None):
        """

        :param data: an int, float, or any other comparable value
        :param curr:
        :return: None but midifies tree to have an additional node
        """
        self.size += 1
        new_node = RBNode(data)
        # Base Case - Nothing in the tree
        if self.root == None:
            new_node.red = False
            self.root = new_node
            return
        # Search to find the node's correct place
        currentNode = self.root
        while currentNode != NIL:
            potentialParent = currentNode
            if new_node.data < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        # Assign parents and siblings to the new node
        new_node.parent = potentialParent
        if new_node.data < new_node.parent.data:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node
        self.fix_tree_after_add(new_node)

    def contains(self,data, curr=None):
        """

        :return:
        """
        if curr == None:
            curr = self.root
        while curr != NIL and data != curr.data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def fix_tree_after_add(self,new_node):
        """
        This method is meant to check and rebalnce a tree back to satisfying all of the red-black properties
        :return:
        None, but modifiex tree
        """
        print("Tree is being fixed!")
        while new_node.parent.red == True and new_node != self.root:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.red:
                    # This is Case 1
                    new_node.parent.red = False
                    uncle.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        # This is Case 2
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    # This is Case 3
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.red:
                    # Case 1
                    new_node.parent.red = False
                    uncle.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        # Case 2
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    # Case 3
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.left_rotate(new_node.parent.parent)
        self.root.red = False



    def delete(self):
        """

        :return:
        """
        pass
    def left_rotate(self,new_node):
        """

        :return:
        """
        print("Rotating left!")

        sibling = new_node.right
        new_node.right = sibling.left
        # Turn sibling's left subtree into node's right subtree
        if sibling.left != None:
            sibling.left.parent = new_node
        sibling.parent = new_node.parent
        if new_node.parent == None:
            self.root = sibling
        else:
            if new_node == new_node.parent.left:
                new_node.parent.left = sibling
            else:
                new_node.parent.right = sibling
        sibling.left = new_node
        new_node.parent = sibling

    def right_rotate(self,new_node):
        """

        :return:
        """
        print("Rotating right!")
        sibling = new_node.left
        new_node.right = sibling.right
        # Turn sibling's left subtree into node's right subtree
        if sibling.right != None:
            sibling.right.parent = new_node
        sibling.parent = new_node.parent
        if new_node.parent == None:
            self.root = sibling
        else:
            if new_node == new_node.parent.right:
                new_node.parent.right = sibling
            else:
                new_node.parent.left = sibling
        sibling.right = new_node
        new_node.parent = sibling

    def get_all_nodes(self):
        """

        :return:
        """
        pass
    def is_red(self):
        """
        This is the class that usually decides that a node is wither red or black, some implementations take the ecurrtra
        bit and will implement an is_black method for additional clarity.
        Generally, True == Red and False == Black

        :return:
        """
        return self.root != None and self.root.red == 1;
    def is_black(self):
        """
        Note that this method is not necessary as some implementations only check is the is_red class method is True or False
        :return:
        True if the node is black or is a leaf
        """
        return self.root != None and self.root.black == 1;


if __name__ == "__main__":
    tree = RedBlackTree()
    tree.add(1)
    # print(tree.root)
    tree.add(3)
    tree.add(4)
    tree.add(3)
    tree.add(4)
    print(tree)
    print(tree.contains(3))
    print(tree.root)