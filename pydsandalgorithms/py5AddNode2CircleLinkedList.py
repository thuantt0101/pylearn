
class Node():

    # Constructor for Node 
    def __init__(self, data):
        self.data = data
        self.next = None # pointer


class CircularLinkedList():

    def __init__(self):
        
        self.last = None

    def addToEmpty(self, data):

        new_node = Node(data)
        
        # create the link
        self.last = new_node
        self.last.next = new_node
        new_node.next = new_node

    def addToBegin(self, data):

        # create new node
        new_node = Node(data)

        # link the next of new node to the first node
        new_node.next = self.last.next

        # link the next of the last node to the new node
        self.last.next = new_node

    def addToLast(self, data):

        # create new node
        new_node = Node(data)

        # link new node to the first node
        new_node.next = self.last.next

        # link the last node to new node
        self.last.next = new_node

        # set the last node  = new node
        self.last = new_node


    def addAfter(self, data, item):

        if self.last == None:
            return 

        new_node = Node(data)
        prev = self.last.next

        while(prev):

            if prev.data == item:
                new_node.next = prev.next
                prev.next = new_node  

                if prev == self.last:
                    self.last = new_node
                    return
                                                                         
            else:                            
                prev = prev.next

            if prev == self.last.next:
                print(item, "is not found in the list")

    def printList(self):

        tmp = self.last.next
        
        while(tmp):
            
            print(tmp.data)        
            
            if tmp == self.last:
                break
            else:
                tmp = tmp.next
        
                
if __name__ =="__main__":

    cllist = CircularLinkedList()
    cllist.addToEmpty(2)
    cllist.addAfter(3, 2)
    cllist.addToBegin(1)
    cllist.addToLast(4)
    cllist.printList()
    




    
            