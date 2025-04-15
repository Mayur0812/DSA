class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

    def printll(self, head):
        curr =head 
        while curr!=None:
            print(curr.val)
            curr = curr.next
        
    def hare_tor(self,head):
        hare = head.next.next
        tor = head.next

        while hare.next!=None and tor!=None:
            print(f"tortoise: {tor.val} Hare: {hare.val}")
            if(hare==tor and tor!=head):
                print(f"Loop exists")
                tor = head
                while(tor!=hare):
                    print(f"Tor: {tor.val} Hare: {hare.val}")
                    tor = tor.next
                    hare = hare.next
                print(f"Loop starts at: {tor.val}")
                return
            hare = hare.next.next
            tor = tor.next
        print("Loop doesn't exist")


if __name__=='__main__':
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    Node6 = Node(6)

    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node5
    Node5.next = Node6
    Node6.next = Node4

    Node1.hare_tor(Node1)

