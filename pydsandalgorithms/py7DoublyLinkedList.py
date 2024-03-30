
# So với Linked List thì Doubly Linked List sẽ chứa thêm 1 con trỏ phụ, thường được gọi là previous pointer.
# ( Con trỏ trỏ đến node trước đó ), con trỏ previous pointer này cùng với next pointer and data chứa dữ liệu/ giá trị
# của node ( 2 thành phần này đều nằm trong 1 node của linked list thông thường ) sẽ là những thành phần tạo nên 
# doubly linked list

# Advantage of DLL

# 1. Chúng ta có thể duyệt duyệt xuôi chiều, hoặc ngược chiều trên danh sách đều được
# 2. Thao tác delete Node trong DLL sẽ hiệu quả hơn vì chúng ta có được con trỏ đến Node cần xoá 
# 3. Chúng ta có thể chèn thêm 1 node mới vào trước 1 node cụ thể nào đó một cách nhanh chóng. 
# trong linked list thông thường, để xoá 1 node chúng ta cần phải biết được con trỏ trỏ đến
# node nằm trước node muốn xoá, đôi khi chúng ta phải duyệt cả danh sách.
# Trong DLL, chúng ta có thể có được node trước node cần xoá bằng cách dùng con trỏ previous node.


# Dis-Advantage of DLL vs Linked List

# 1. Mọi node nằm trong DLL đều yêu cầu thêm không gian dành cho một con trỏ previus. Tuy nhiên ta vẫn có thể
# cài đặt DLL với 1 con trỏ duy nhất , vẫn có cách làm điều đó.

# 2. Tất cả các thao tác đều yêu cầu phải duy trì thêm một con trỏ là previous. Ví dụ khi thực hiện chèn thêm
# 1 node vào DLL, chúng ta phải chỉnh con trỏ previos cùng với các con trỏ next. 


# Thao tác chèn thêm 1 node mới vào DLL

# Chèn thêm vào đầu DLL
# Chèn thêm vào phía sau 1 node cụ thể
# Chèn thêm vào cuối DLL
# Chèn thêm vào phía trước 1 node cụ thể.


# for garbage collection
import gc

# Thao tác
class Node():

    def __init__(self, data = None, next = None, prev = None):

        self.data = data       
        self.next = next # pointer to the next node        
        self.prev = prev # pointer to the previous node


class DoublyLinkedList():

    def __init__(self):

        self.head = None # head Node ( Con trỏ head )

    
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


if __name__=="__main__":
    
    dll = DoublyLinkedList()
    dll.push(3) # 3
    dll.push(1) # 1 > 3  

    dll.insertAfter(data = 2, prev_node = dll.head)  # 
    dll.append(10)
    dll.append(11)    
    dll.insertBefore(data = 0,before_node = dll.head)
    a = dll.head.next.next.next.next
    dll.insertBefore(data = 4, before_node = a)   
    b = dll.head.next.next.next.next.next.next        
    dll.insertBefore(data = 10.5, before_node = b)   
    dll.printList()    # 0 > 1 > 2 > 3 > 4 > 10 > 10.5 > 11

    print('----------delete test---------')
    dll.deleteNode(dll.head) 
    dll.printList() # 1 > 2 > 3 > 4 > 10 > 10.5 > 11

    print('----------delete middle node test---------')    
    midle = dll.head.next
    print('head.next :' , midle.data)
    print('head.next.prev.data', midle.prev.data)
    print('head.next.next.data', midle.next.data)

    dll.deleteNode(midle)    
    dll.printList()
    size = dll.sizeOfList()
    print(f"size of list is: {size}") # 6

    print('---------------count-size-by-recursive---')
    sizeRec = dll.sizeOfListRec(dll.head.next)
    print(f"count-size-by-recursive : {sizeRec}")

    print('-----------reverse list-----')
    dll.reverseList()
    dll.printList()



