class MyLinked_list:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    
    def get(self,index:int) -> int:
        if (index == 0):
            return 

    def  addAtHead(self, val: int) -> None:
        newNode = MyLinked_list(val)
        #newNode.val = val
        if self.next==None:
            print(f"Adding {self.val}")
            self.head = newNode
        else:
            newNode.next  = self.head
            self.head = newNode
        #self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = MyLinked_list(val)
        if index == 0:
            self.head = newNode
            newNode.next= self.head
            self.head = newNode
        if index >= 1:
            ctr = 0
            ptr = self.head
            while ((ptr.next != None)):
                print(f"Adding after {ptr.val}")
                if(ctr == index):
                    newNode.next = ptr.next
                    ptr.next = newNode
                    break
                else:
                    ptr = ptr.next
                    ctr +=1

    def printLL(self, head):
        curr = head
        while curr !=None:
            print(curr.val, end = ' ')
            curr = curr.next

if __name__== '__main__':
    ll = MyLinked_list('0')
    ll.next = MyLinked_list('1')
    ll.next.next = MyLinked_list('2')
    ll.next.next.next = MyLinked_list('3')
    
    ll.printLL(ll)







    
        


                


