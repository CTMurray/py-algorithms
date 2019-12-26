# The basic operations supported are by binary trees are
# searching, traversal, insertion, and deletion.
# printing inorder, preorder, and postorder.

from BSTNode import BSTNode

class BST:
    #create an empty tree with a root node
    def __init__(self):
        self.root = BSTNode(None)
        #node count
        self.count = 0

    def insert(self, data):

        if self.root.data == None:
            self.root.data = data
            self.count += 1
            return

        # pointer to root of tree
        temp = self.root

        while temp is not None:

            # traverse left sub tree
            if data < temp.data:
                # if empty left child
                if temp.left == None:
                    temp.left = BSTNode(data)

                    prev = temp
                    temp = temp.left
                    self.count += 1
                    return
                else:
                    temp = temp.left

            elif data > temp.data:
                # empty right child
                if temp.right == None:
                    temp.right = BSTNode(data)
                    prev = temp
                    temp = temp.right
                    self.count += 1
                    return
                else:
                    temp = temp.right

            else:
                print("Duplicate entry {0}".format(data))
                break


    #check if empty
    #Traverse left
    #Visit node - print data
    #traverse right
    #left – root – right
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    #check if empty
    # Visit node - print data
    # Traverse left
    # traverse right
    # root – Left – right
    def preorder(self, node):
        if node is None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    # check if empty
    # Traverse left
    # traverse right
    # Visit node - print data
    # Left – right - root
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)


if __name__ == "__main__":
        BST = BST()

        BST.insert(10)
        BST.insert(5)
        BST.insert(15)
        BST.insert(1)
        BST.insert(9)
        BST.insert(1) #test duplicate
        BST.insert(14)
        BST.insert(20)

        #BST Layout
                    #10
            #5              #15
        #1      #9      #14     #20


        print("Node count is ", BST.count)
        print("=============Preorder===================")
        #expected output 10, 5, 1, 9, 15, 14, 20
        BST.preorder(BST.root)
        print("=============Inorder===================")
        #expected output 1, 5, 9, 10, 14, 15, 20
        BST.inorder(BST.root)
        print("=============Postorder===================")
        #expected output 1, 9, 5, 14, 20, 15, 10
        BST.postorder(BST.root)


