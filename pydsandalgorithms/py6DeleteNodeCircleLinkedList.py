
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


    def deleteNode(self, key):
        
        # get head node
        prev = self.last.next

        while(prev):
            
            current = prev.next

            if current.data == key :                
                if current == self.last:                    
                    prev.next = current.next                    
                    current = None
                    self.last = prev                                                  
                else:
                    prev.next = current.next
                    current  = None
                    
                return          
            
            prev = prev.next
            
            if prev == self.last.next:
                return

        print(f"key : {key} is not found")


    def sizeOfList(self):        
        if self.last is None:
            return  0 
        
        temp = self.last.next
        size = 0
        while(temp):
            size += 1
            temp = temp.next
            if temp == self.last.next:
                break

        return size

    def sizeOfListRec(self, node):

        if node == self.last:
            return 1
                        
        return 1 + self.sizeOfListRec(node.next)
        
    def size(self):
        return self.sizeOfListRec(self.last.next)


    def findOne(self, key) :

        temp = self.last.next
        
        while(temp):
            
            if temp.data == key:
                return temp

            temp = temp.next

            if temp == self.last.next:
                return None
            
    # node default is Head node
    def findOneRec(self, key, node):

        if node is None:
            return None
        
        if node.data == key:
            return node
        
        # if current node is last --> stop calling recursive
        if node == self.last:
            return None
        else : 
            return self.findOneRec(key, node.next)
        
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
    cllist.deleteNode(4)
    cllist.printList()
    print(f"size of list : {cllist.sizeOfList()}")
    print(f"size of list [recursize math] : {cllist.size()}")
    find1 = cllist.findOne(4)
    
    if (find1) :
        print(find1.data)    
    else:
        print('No one is found')

    find2 = cllist.findOneRec(key=3, node = cllist.last.next)

    if not find2 :
        print(f"find2 value is not found")
    else:
        print(f"find2 value is : {find2.data}")



    
            