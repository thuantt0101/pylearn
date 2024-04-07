
import gc

class Node():

    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    

class DoublyLinkedList():

    def __init__(self):
        self.head = None
    # Push new node to the head of Doubly Linked List
    def push(self, data):        
        """ Thuật toán
            Step 1 : Cấp phát bộ nhớ cho node mới
            Step 2 : Truyền dữ liệu(chính là giá trị int ) vài node mới
            Step 3 : Làm cho con trỏ next của node mới trỏ đến con trỏ Head của DLL, và làm cho con trỏ previous của node mới = Null
            Step 4 : Làm cho con trỏ previous của node head trỏ đến node mới
            Step 5 : Làm cho con trỏ head trỏ đến node mới được chèn vào.
        """
        # step 1 & 2
        new_node = Node(data)
        
        head = self.head
        
        if (head):
            new_node.next = head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node

    def insertAfter(self, data, prev_node):
        """ Thuật toán
            Step 1: Kiểm tra pre_node có tồn tại không, nếu không tồn tại thì return luôn
            Step 2: Cấp phát bộ nhớ cho node mới
            Step 3: Thêm dữ liệu cho node mới
            Step 4: Làm cho con trỏ next của node mới trỏ đến con trỏ next của prev node
            step 5: Làm cho con trỏ previous của node mới trỏ đến previous node 
            Step 6: Làm cho con trỏ next của prev node trỏ đến node mới
            Step 7: Làm cho con trỏ previous của node next trỏ đến node mới                         
        """

        # Step 1 : Check if the given previous node is null
        if prev_node is None:
            return
        
        # step 2 & 3: allocate & put in the data
        new_node = Node(data= data)

        # step 4: 
        new_node.prev = prev_node

        # step 5: 
        new_node.next = prev_node.next

        # step 6: 
        prev_node.next = new_node

        # step 7:
        if new_node.next is not None:
            new_node.next.prev = new_node
                
    def append(self, data):

        """ Thuật toán
            Step 1 : Cấp phát bộ nhớ cho node mới
            Step 2 : Truyền giá trị vào node mới
            Step 3 : Làm cho con trỏ next của node mới  thành null             
            Step 4 : Nếu DLL đang trống thì 
                Step 4.1 : Làm cho con  trỏ head của DLL trỏ đến New Node
                Step 4.2 : Làm cho con trỏ prev của New_Node thành Null                                         
            Step 5 : Nếu Danh sách không trống thì:
                Step 5.1 : Làm cho con trỏ prev của New_Node trỏ đến node cuối cùng hiện tại
                Step 5.2 : Làm cho con trỏ next của node cuối cùng hiện tại trỏ đến new_node                            
        """
                
        new_node = Node(data)
        temp = self.head
        
        if temp is None:
            self.head = new_node
            return
        
        while(temp):
            
            if temp.next is None:
                new_node.prev = temp
                new_node.next = None
                temp.next = new_node
                break
            
            temp = temp.next
                
    # insert a node before specific node
    def insertBefore(self, data, before_node):
        
        """ Thuật toán
            Step 1 : Kiểm tra before node có null không, nếu null thì return luôn
            Step 2 : Cấp phát bộ nhớ cho node mới
            Step 3 : Thêm dữ liệu vào node mới            
            Step 4 : Nếu before node là Head node thì
                Step 4.1 : Làm cho con trỏ next của new_node trỏ về head node
                Step 4.2 : Làm cho con trỏ prev của head_node trỏ về new_node            
                Step 4.3 : Làm cho con trỏ head của Doubly Linked List trỏ về new_node
            Step 5: Nếu before không phải là head node
                Step 5.1 : Làm cho con trỏ next của new_node trỏ đến before_node 
                Step 5.2 : Làm cho con trỏ prev của new_node trỏ đến previous của node before_node                
                Step 5.3 : Làm cho con trỏ next của prev_node của before_node trỏ đến new_node
                Step 5.4 : Làm cho con trỏ prev của before_node trỏ đến new_node
        """
        
        if before_node is None:
            return
        
        new_node = Node(data)

        if before_node == self.head:
            new_node.next = before_node
            before_node.prev = new_node
            self.head = new_node
        else :
            new_node.next = before_node
            new_node.prev = before_node.prev
            before_node.prev.next = new_node
            before_node.prev = new_node
                    
    def deleteNode(self, delete_node):
        """ Thuat toan :
            Step 1 : if delete_node is head_node:
                Step 1.1 : Set head pointer to next_node of delete_node
                Step 1.2 : Set   
        """
        if (not delete_node):
            return
        
        head = self.head
        
        # 1 > 2 > 3 ==> 2 > 3
        # delete node is head node
        if delete_node == head:
            next = head.next
            next.prev = None                        
            delete_node = None
            self.head = next            
        else: # delete node is different from head node
            prev = delete_node.prev            
            next = delete_node.next 
            
            # release delete_node from memory 
            delete_node = None                       
                                         
            if (next):
                next.prev = prev          

            prev.next = next                                

        # call the python garbage collection
        gc.collect()
                    

    # use while loop to count size of list
    def sizeOfList(self):

        temp = self.head        
        size = 0
                
        while(temp):
            size += 1
            temp = temp.next

        return size
    
    # use recursive algorithm tho count number of items in list
    def sizeOfListRec(self, node):
        """
        @param [node] : node that you want to count from to the end
        
        """    

        if node is None:
            return 0
        
        return 1 + self.sizeOfListRec(node.next)

    def reverseList(self):

        # present    : 1 > 2 > 3 > 4
        # want to be : 4 > 3 > 2 > 1
        
        temp = self.head
        
        while(temp):
            next = temp.next

            temp.next = temp.prev
            temp.prev = next

            if next is None:
                self.head = temp

            temp = next            


    # A utility function to find last node of linked list
    def lastNode(self, node):
        
        while(node.next != None):
            node = node.next
        
        return node

    # Considers last element as pivot, places the pivot element at its
    # correct position in sorted array, and places all smaller (smaller than
    # pivot) to left of pivot and all greater elements to right of pivot 
    def partition(self, l , h):

        # set pivot as h element
        pivot = h.data

        # similar to i = l-1 for array implementation
        i = l.prev

        j = l

        while j != h :

            if j.data <= pivot:

                i = l if (i == None) else i.next
                temp = i.data
                i.data = j.data
                j.data = temp
            j = j.next

        i = l if (i == None) else i.next
        temp = i.data
        i.data = h.data
        h.data = temp

        return i
    
    # A recursive implementation of quicksort for linked list 
    def _quickSort(self, left, right):

        if right != None and left != right and left !=right.next:
            temp = self.partition(left, right)
            self._quickSort(left, temp.prev)
            self._quickSort(temp.next , right)

    def quickSort(self, node):

        # Find last node
        head = self.lastNode(node)

        self._quickSort(node, head)


    def printList(self):
        """ print data of Doubly Linked List from head node
            if Dll is None --> Print empty msg
        """

        temp = self.head

        if( not temp ):
            print(f"the list is empty")
            return

        while(temp):
            print(temp.data)        
            temp = temp.next                 
        

if __name__ =='__main__':
    
    dll = DoublyLinkedList()
    dll.push(10)
    dll.push(5)
    dll.push(30)
    dll.push(2)
    dll.quickSort(dll.head)    
    dll.printList()


