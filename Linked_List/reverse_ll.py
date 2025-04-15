class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

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

    def reverse(self, head):
        if head == None:
            print("Returning Null from reverse")
            return None
    
        curr = head
        prev = None
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
    

if __name__ == '__main__':
    root = Node(1)
    root= root.insertatFront(root,2)
    root=root.insertatFront(root,3)
    root=root.insertatFront(root,4)
    root.printll(root)
    out = root.reverse(root)
    print("")
    print(out.printll(out))
    
    
    
    
            

        