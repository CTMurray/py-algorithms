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

    # start at the root then print and return True if found
    def find(self, node, value):
        if node == None:
            return

        if node.data == value:
            print("Found {0}".format(value))
            return True

        if value < node.data:
            return self.find(node.left, value)
        else:
            return self.find(node.right, value)

    def delete_node(self, node, value):
        #if root doesn't exist return
        if not node:
            return

        if node.data == value:
            # case leaf node
            if node.left is None and node.right is None:
                print("Deleted {0}".format(value))
                node.data = None
                self.count -= 1
                return

            # case of one child
            if node.left and node.right is None:
                node.data = node.left.data
                self.count -= 1
                return

            if node.right and node.left is None:
                node.data = node.right.data
                print("Deleted {0}".format(value))
                node.right.data = None
                self.count -= 1
                return

            # case two children
            if node.left and node.right:
                temp = node.right
                min = temp.data
                while temp.left:
                    temp = temp.left
                    min = temp.data

                node.data = min
                self.delete_node(node.right, node.data)

        if value < node.data:
            return self.delete_node(node.left, value)
        else:
            return self.delete_node(node.right, value)

                #BST Layout
                    #10
            #5              #15
        #1      #7      #14     #20
                    #9

if __name__ == "__main__":
        BST = BST()

        BST.insert(10)
        BST.insert(5)
        BST.insert(15)
        BST.insert(1) #comment out for one child delete
        #BST.insert(9)
        BST.insert(7)
        #BST.insert(1)  # test duplicate
        BST.insert(14)
        BST.insert(20)

        #should print 9
        #print(BST.find(BST.root, 9))

        #case leaf node
        #BST.delete_node(BST.root, 9)
                # BST Layout
                    # 10
            # 5              #15
        # 1      #7      #14     #20
                    # None

        # case one child
        #BST.delete_node(BST.root, 5)



        #case two child
        #BST.delete_node(BST.root, 5)

        #BST Layout
                    #10
            #7              #15
        #1      #9      #14     #20


        print("Node count is ", BST.count)
        print("=============Preorder===================")
        #expected output 10, 5, 1, 9, 7, 15, 14, 20
        BST.preorder(BST.root)
        print("=============Inorder===================")
        #expected output 1, 5, 7, 9, 10, 14, 15, 20
        BST.inorder(BST.root)
        print("=============Postorder===================")
        #expected output 1, 7, 9, 5, 14, 20, 15, 10
        BST.postorder(BST.root)


