class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

    def detect_loop(self,head):
        if head == None:
            return
        slow = head.next
        fast = slow.next
        count = 0
        while slow!=None or fast.next!=None:
            slow = slow.next
            fast = fast.next.next

            if(slow==fast):
                print("Loop Exists")
                slow = slow.next
                count = 1
                while slow!=fast:
                    count+=1
                    slow = slow.next
                return count
    

if __name__=='__main__':
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    Node6 = Node(6)
    Node7 = Node(7)

    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node5
    Node5.next = Node6
    Node6.next = Node7
    Node7.next = Node2

    print(f"length of loop is :{Node1.detect_loop(Node1)}")