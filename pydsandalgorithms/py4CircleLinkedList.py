# https://cafedev.vn/ctdl-gioi-thieu-circular-linked-list-danh-sach-lien-ket-vong/

# Circle linked list là 1 danh sách liên kết đơn ( linked list ) trong đó tất cả các node được
# liên kết với nhau thành vòng tròn. Sẽ không có con trỏ Null ở cuối Circle linked list 

# Một Circle Linked List  có thể ở dạng danh sách liên kết vòng đơn ( single circle linked list ) or doubly circle linked list


# Ưu điểm của circle linked list

# 1. 
# Bất kỳ node nào cũng có thể là điểm bắt đầu ( starting node ). Chúng ta có thể duyệt toàn bộ danh sách bằng cách bắt đầu tại 1 node bất
# kỳ. Chúng ta chỉ cần dừng lại khi node đầu được duyệt lại được duyệt thêm lần nữa.

# 2. 
# Circle linked list rất hữu dụng trong việc triển khai queue - hàng đợi. Khi triển khai danh sách vòng để cài đặt queue.
# chúng ta sẽ không cần duy trì 2 điểm front ( điểm đầu ) và rear ( điểm cuối ) của queue. Chúng ta chỉ duy trì 1 con trỏ dành
# cho node mới nhất được truyền vào ( nằm ở cuối danh sách ) Lấy node cuối cùng này làm mốc, ta có thể dễ dàng truy cập đến node
#  ở đầu danh sách.


# 3. Circle linked list còn hữu dụng trong các ứng dụng phần mềm, để lặp đi lặp lại danh sách. Ví dụ, khi nhiều ứng dụng đang chạy trên 1
# máy tính, thông thường Hệ điều hành sẽ đặt các ứng dụng đang chạy trong 1 danh sách, và sau đó duyệt qua chúng, mỗi lần duyệt đến ứng
# dụng nào thì cho ứng dụng đó 1 khoảng thời gian để thực thi, và sau đó lại đưa chúng vào danh sách đợi trong khi CPU lại cấp 
# cho 1 ứng dụng khác. Vì thế sẽ rất lý tưởng khi hệ điều hành sử dụng một danh sách liên kết vòng để khi duyệt đến cuối danh sách
# nó có thể quay vòng về phía trước danh sách/ phần đầu danh sách.

# 4. 
# Circle doubly linked list được sử dụng để cài đặt các cấu trúc dữ liệu nâng cao ( Ví dụ Fibonacci  Heap )



class Node():


    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList():
    
    # Constructor to create new empty Circle Linked List
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # Circle linked list
    def push(self, data):
        node = Node(data)
        
        temp = self.head
        node.next = temp

        # if linked list is not None then set the next 
        # of the last node
        if self.head is not None:
            # assign last node to temp
            while(temp.next != self.head):
                temp = temp.next 

            # set next of last node to head node
            temp.next = node
        else:
            node.next = node
            self.head = node

    
    def printList(self):

        temp = self.head
        head = self.head

        while(temp):
            print(temp.data)
            # if current is head then stop loop            
            if temp.next == head:
                break
            temp = temp.next        

            

    # Function to insert new node to the Circular linked list
    # 1. Insert to the last node        
    # 2. Insert node to Null list
    # 3. Insert node to first node
    # 4. Insert node to middle list                        
    def insert(self, data, prev_node):
        
        new_node = Node(data)
        temp = self.head
        head = self.head
        

        while(temp):
            
            # find last node then set next node to new_node
            # and then set next new node to the head
            if(temp.next == head):
                new_node.next = head
                temp.next = new_node
                break
                
                        


if __name__=="__main__":
    clList = CircularLinkedList()
    clList.push(2)
    clList.push(4)
    
    clList.printList()

            

        
