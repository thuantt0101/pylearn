# https://cafedev.vn/ctdl-danh-sach-lien-ket-don-linked-list-phan-1-gioi-thieu/

# Danh sách liên kết đơn  - Linked List

# Giống như kiểu dữ liệu array (mảng), Linked List là một cấu trúc dữ liệu tuyến tính. 
# Tuy nhiên khác với array, các phần tử của linked list không được lưu trữ tại các vị trí 
# ô nhớ liền kề nhau, mà các phần tử của linked list sẽ được liên kết với nhau bằng cách sử dụng các con trỏ.

#  ------------     ---------------
# |  A  |     | -> |   B    |      |    ......  Null
# ------------     ----------------
# Data  Next

# Con trỏ : Nó sẽ lưu địa chỉ của biến mà nó lưu trữ

# 1/ Tại sao lại dùng linked list

# Array có thể được sử dụng để lưu trữ dữ liệu thuộc cùng 1 kiểu dữ liệu ( Python có thể lưu nhiều kiểu ), một cách tuyến tính, nhưng array tồn tại các vấn đề sau:
# 1. Kích thước của array là cố định vì vậy chúng ta phải biết trước giới hạn trên (upper limit) về số phần tử.
# Ngoài ra chúng ta phải cấp phát số lượng ô nhớ = với giới hạn trên về số phần tử, bất kể ta có sử dụng hết ô nhớ đó hay không.

# 2. Việc chèn thêm 1 phần tử mới vào array tốn khá nhiều công đoạn, vì chúng ta sẽ phải tạo chổ chứa cho phần tử mới,
# và để tạo ra chổ chứa này thì các phần tử hiện tại trong mảng phải được dịch chuyển ( dịch sang trái hoặc dịch sang phải tùy trường hợp )

# Ví dụ : Trong 1 hệ thống, nếu chúng ta duy trì 1 danh sách đã được sắp xếp IDs bên trong 1 mảng là id[]
ids = [1000, 1010, 1005, 2000, 2040]
# Nếu chúng ta muốn chèn thêm 1 ID là 1005 vào mảng ids, vậy nếu muốn duy trì được thứ tự đã sắp xếp của mảng, chúng ta phải dịch chuyển
# tất cả các phần tử nằm sau 1000 sang phải.

# Việc xóa 1 phần tử khỏi mảng cũng khá mất công , trừ khi sử dụng 1 số kỹ thuật đặc biệt, Ví dụ xóa 1010 ra khỏi ids thì mọi phần tự sau ID = 1010
# Phải được dịch chuyển sang trái.

# Ưu điểm của Linked List vs Array

# 1. Linked list có kích thước động
# 2. Dễ dàng chèn thêm phần tử vào mảng và xóa phần tử khỏi mảng

# Hạn chế của Linked List

# 1. Khổng thể truy cập ngẫu nhiên ( random access ). Chúng ta phải truy cập 1 cách tuần tự, bắt đầu từ node đầu tiên.
# Vì vậy chúng ta sẽ không thể tìm kiếm nhị phân( Binary search) với Linked List một cách hiệu quả.

# 2. Mỗi phần tử của Linked List đều chứa 1 con trỏ ( pointer ) cần phải cấp phát bộ nhớ cho con trỏ này.

# 3. Linked List không thân thiện với bộ nhớ cache. Bởi vì các phần tử trong Array được bố trí nằm liền kề, 
# liên tiếp nhau, nên chúng ta có thể dễ dàng truy cập đến các phần tử của Array thông qua các vị trí 
# tham chiếu được thể hiện bằng các chữ số, trong khi đó điều này là không thể đối với Linked List.


#--------Mô tả---------------------
# Một Linked List (danh sách liên kết) sẽ được biểu diễn bởi một con trỏ (pointer) trỏ đến node 
# đầu tiên của Linked List đó. Node đầu tiên của Linked List được gọi là node head. Nếu Linked List là trống, giá trị của node head sẽ là NULL.

# Mỗi node ở bên trong một Linked List sẽ bao gồm ít nhất hai thành phần sau:

# 1. data (dữ liệu, có thể là kiểu số, kiểu ký tự, …)

# 2. pointer (con trỏ) hoặc có thể hiểu là reference (tham chiếu) tới node tiếp theo trong Linked List.


class Node:
    
    # Function to initiatelize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initiatelize next as Null


# Linked List class
class LinkedList:
    
    # Function to initiateline Linked List Object
    def __init__(self):
        self.head = None

    # This function prints contents of linked list 
    # starting from head
    def print_linkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def push(self, data):        

        # create a new head node        
        new_head = Node(data)

        # Make next of new Node as head
        new_head.next = self.head

        # Move the head to point to new Node
        self.head = new_head     

    def insert_after(self, data, prev_node):        
        #Thuật toán:

        # 1. Kiểm tra tham số con trỏ pre_node có Null hay không, nếu Null chúng ta sẽ return luôn
        temp = self.head
        is_exists = False
        while(temp):
            if temp == prev_node:
                is_exists = True
                break
            else:
                temp = temp.next            
                        
        if is_exists == False:
            print("The given previous node must LinkedList")
            return
       
        # 2. Cấp phát bộ nhớ cho Node mới
        # 3. Truyền dữ liệu vào Node mới
        new_node = Node(data)            

        # 4. Làm cho con trỏ next của Node mới = con trỏ Pre_Node
        new_node.next = prev_node.next
        
        # 5. Làm cho con trỏ next của Pre_Node = Node mới
        prev_node.next = new_node

    def append(self, data):
        # Thuật toán
        
        # 1. Tìm kiếm final Node 
        temp = self.head
        final_node = None
        while(temp):
            next = temp.next
            if next == None:
                final_node = temp
            temp = next
                
        # 2. Insert after
        self.insert_after(data = data, prev_node=final_node)

    def delete_node(self, key):
        
        # 2. Link the next Node of prev_node to delete next node.
        # 3. Giải phóng bổ nhớ cho delete node
                
        temp = self.head

        # 1. If the head node itselt holds the key to be deleted
        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        # 2. Find first occurence of key &  prev_node in linked list      
        while(temp):
            if temp.data == key:
                break
            prev_node = temp
            temp = temp.next
        
        if temp == None:
            return
        
        # Unlink the node from linked list  
        prev_node.next = temp.next

        # Giải phóng bộ nhớ.
        temp == None


    '''
        get size of linked list using while
    '''        
    def get_count(self):
        temp = self.head
        size_of_llist = 0
        
        if temp != None:
            while(temp):
                size_of_llist += 1
                temp = temp.next

        return size_of_llist   
    

    # This function checks whether the value
    # key present in the linked list
    def find_one(self, key):
        temp = self.head        
        
        while(temp):
            if temp.data == key:               
                return True                
            else:
                temp = temp.next

        return False 

    def find_one_rec(self, node , key):                
        
        if (not node):
            return False

        if node.data == key:            
            return True
        else:            
            return self.find_one_rec(node.next, key)        

        
    def find(self, key):    
        head = self.head
        if (not head) :            
            return False
        else:            
            return self.find_one_rec(head, key)        

    # This function counts number of nodes in Linked List 
    # recursively, given 'node' as starting node.        
    def get_count_rec(self, node):
        
        if not node: # base case
            return 0
        else:
            return 1 + self.get_count_rec(node.next)
            # 1 + self.get_count_rec(node.next)
            # 1 + 1 + self.get_count_rec(node.next)
            # 1 + 1 + 1 + self.get_count_rec(node.next)
            # ...            
        

    '''
        get size of linked list using recursion 
    '''
    def get_size(self):
        return self.get_count_rec(self.head)

        
    def reverse(self):
        
        prev = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = prev
    
            # dịch chuyển prev & current sang phải
            prev = current
            current = next
        
        self.head = prev
        

    


                
if __name__=="__main__":

    """
    # Start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''
    llist.head.next = second # Link first node with second  

    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    second.next = third # Link second node with the third node 

    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    print(type(llist)) # <class '__main__.LinkedList'>
    print(type(llist.head)) # <class '__main__.Node'>
    llist.print_linkedlist()

    print('----------------------')
    llist.push(0)
    llist.print_linkedlist()    
    """
    

    # Testing 2
    llist = LinkedList()
    llist.push(6) # 6 > None
    llist.push(7) # 7 > 6 > None
    llist.push(1) # 1 > 7 > 6 > None
    llist.insert_after(data=8, prev_node = llist.head.next) # 1 > 7 > 8 > 6 > none
    llist.append(9) # 1 > 7 > 8 > 6 > 9 > none
    llist.append(10) # 1 > 7 > 8 > 6 > 9 >  10 > none
    llist.print_linkedlist()
    print('------------------------')
    llist.delete_node(key=9)
    llist.print_linkedlist() # 1 > 7 > 8 > 6 >  10 > none
    size_of_llist = llist.get_count()
    print('-------------------------')
    print(f"size_of_llist : {size_of_llist}")
    size_of_llist = llist.get_size()
    print(f"size of linked list by recusive : {size_of_llist}")
    print(f"search 7 to check whether 7 present in linked list? {llist.find_one(key=7)}")
    print(f"search 7 to check whether 7 present in linked list? {llist.find(key=7)}")
    print(f"search 9 to check whether 9 present in linked list? {llist.find_one(key=9)}")
    print(f"search 9 to check whether 9 present in linked list? {llist.find(key=9)}")

    print('--------------------------')
    llist.reverse()
    llist.print_linkedlist()    





