class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None


    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def search(self,x):
        i=self.head
        while i!=None:
            if i.data==x:
                return True
            i=i.next
        return False
    if __name__=='__main__':
        llist=ll()
        
        llist.push(10);
        llist.push(30);
        llist.push(8);
        llist.push(15);
        llist.push(23);
        if llist.search(23):
            print("Element present in the linked list"
                  )
        else:
            print("No")      
                  
