class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

    def inters(self, head1, head2):
        if head1==None or head2==None:
            return None
    
        while((head1) and (head2)):
            if(head1.val==head2.val):
                print(head1.val,end= "--->")
                head1= head1.next
                head2 = head2.next
            elif(head1.val>head2.val):
                head2 = head2.next
            else:
                head1 = head1.next


if __name__ == "__main__":
    root1 = Node(1)
    root1.next = Node(2)
    root1.next.next= Node(3)
    root1.next.next.next = Node(4)
    root1.next.next.next.next  = Node(5)


    root2 = Node(2)
    root2.next = Node(3)
    root2.next.next= Node(4)

    root1.inters(root1,root2)





