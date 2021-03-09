class Node(): 
 
    def __init__(self, data): 
        self.key = data
        self.left = None
        self.right = None
def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left) 
    print(temp.key,end = " ")
    inorder(temp.right) 
 
def insert(temp,key):
 
    if not temp:
        root = Node(key)
        return
    k = [] 
    k.append(temp)  
    while (len(k)): 
        temp = k[0] 
        k.pop(0) 
 
        if (not temp.left):
            temp.left = Node(key) 
            break
        else:
            k.append(temp.left) 
 
        if (not temp.right):
            temp.right = Node(key) 
            break
        else:
            k.append(temp.right) 
     
if __name__ == '__main__':
    root = Node(10) 
    root.left = Node(11) 
    root.left.left = Node(7) 
    root.right = Node(9) 
    root.right.left = Node(15) 
    root.right.right = Node(8) 
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root) 
 
    key = 12
    insert(root, key) 
 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
