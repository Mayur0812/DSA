class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None

    def insertatFront(self,root,val):
        if root == None:
            return None
        
        temp = Node(val)
        temp.next = root
        return temp
    
    def printll(self, head):
        if (head==None):
            print("Empty list")
            return
        
        curr = head
        while curr!= None:
            print(curr.val, end = " ")
            curr = curr.next

    def getSize(self, head):
        size_ = 0
        while head!=None:
            head = head.next
            size_+=1

        return size_


if __name__=='__main__':
    root = Node(1)
    root= root.insertatFront(root,2)
    root=root.insertatFront(root,3)
    root=root.insertatFront(root,4)
    root=root.insertatFront(root,5)
    size_ = root.getSize(root)
    print(f"Size is {size_}")
    