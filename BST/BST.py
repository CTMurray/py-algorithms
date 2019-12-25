from BSTNode import BSTNode

# The basic operations supported are by binary trees are
# searching, traversal, insertion, and deletion.

class BST:
    #create an empty tree with a root node
    def __init__(self):
        self.root = BSTNode(None)
        self.count = 0
        # self.head = None
        # self.parent = None
        # self.data = None
        # self.left = None
        # self.right = None

    def insert(self, data):

        if self.root.data == None:
            self.root.data = data
            self.count += 1
            return

        # pointer to root of tree
        temp = self.root
        while temp is not None:

            #node to insert
            new_node = BSTNode(data)

            # traverse left sub tree
            if data < temp.data:
                #empty left child
                if temp.left == None:
                    temp.left = new_node

                    prev = temp
                    temp = temp.left
                    self.count += 1
                    return

            if data > temp.data:
                # empty right child
                if temp.right == None:
                    temp.right = new_node
                    prev = temp
                    temp = temp.right
                    self.count += 1
                    return




                    #temp.left.parent = temp
                    #self.count += 1
                    #self.root = self.root.left

            #temp = temp.left
    def printTree(self):
        temp = self.root
        if self.root == None:
            print("Empty tree!")

        #printing left subtree
        while temp is not None:
            print(temp.data)
            temp = temp.left



if __name__ == "__main__":
        BST = BST()

        BST.insert(10)
        BST.insert(5)
        print("Node count is ", BST.count)
        BST.printTree()

