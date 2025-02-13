class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("node containing the given value is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("the list is empty...")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found...")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("list is not empty...")

    def delete_first(self):
        if self.head is None:
            print("list is empty...")
            return
        else:
            n= self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("list is empty...")
            return
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_any(self,x):
        if self.head is None:
            print("list is empty...")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data == x:
                    n.ref = n.ref.ref
                    return
                n=n.ref
                if n.ref is None:
                    print("node not present...")



ll1 = linkedList()
ll1.add_empty(1)
ll1.add_end(2)
ll1.add_end(3)
ll1.add_end(4)
ll1.add_end(5)
ll1.delete_any(10)
ll1.print_LL()