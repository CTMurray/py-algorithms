from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    #insert at the end
    def insert_end(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            return
        n = self.head
        while n.next is not None:
            n = n.next

        n.next = item

    #List printing function
    def print_list(self):
        if list.head == None:
            print("List is empty")
            return

        n = self.head
        while n is not None:
            print(n.data)
            n = n.next

    #Deleting by value
    def delete_end(self, number):
        
        #if trying to delete and empty list
        if self.head == None:
            print("List is empty")
            return

        #if the item to be removed is the first item
        if self.head.data == number:
            self.head = self.head.next
            return

        temp = self.head
        while temp is not None:
            #temp.next
            if temp.data == number:
                print("Target is: found")
                break

            #maintain the previous value
            previous = temp
            temp = temp.next

        #Item not found
        if temp == None:
            print("Item {0} not found!" .format(number))
            return

        previous.next = temp.next
        temp = None

if __name__ == "__main__":
    list = LinkedList()

    #add items to list
    for i in range(10):
        list.insert_end(i)

    list.delete_end(0)

    list.print_list()











