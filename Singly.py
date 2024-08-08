class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None
        self.temp = None
    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            value = int(input("Enter a value: "))
            newnode = Node(value)
            if self.head == None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode
    def display(self):
        self.temp = self.head
        while self.temp != None:
            print(self.temp.data)
            self.temp = self.temp.next
    def insertfront(self):
        data = int(input("Enter the front value:"))
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def insertend(self):
        data = int(input("Enter the back value:"))
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            self.temp = self.head
            while self.temp.next != None:
                self.temp = self.temp.next
            self.temp.next = newnode
    def insertmid(self):
        self.temp = self.head
        data = int(input("Enter the mid value:"))
        newnode = Node(data)
        position = int(input("Enter the position:"))
        i = 1
        while i < position :
            if self.temp != None:
                self.temp = self.temp.next
                i += 1
            else:
                newnode.next = self.temp.next
                self.temp.next = newnode
    def deletefront(self):
        self.temp = self.head
        self.head = self.head.next
        del self.temp
    def deleteend(self):
        self.temp = self.head
        if self.head.next == None:
            self.head = None
        else:
            previous = None
            while self.temp.next != None:
                previous = self.temp
                self.temp = self.temp.next
            previous.next = None
        del self.temp
    def deletemid(self):
        position = int(input("Enter the position to delete:"))
        self.temp = self.head
        prev = None
        i = 0
        while i < position and self.temp != None:
            prev = self.temp
            self.temp = self.temp.next
            i += 1
        
        if self.temp == None:
            print("Position is out of bounds")
        else:
            prev.next = self.temp.next
            del self.temp
obj = LinkedList()
obj.create()
obj.insertfront()
obj.insertend()
obj.insertmid()
obj.deletefront()
obj.deleteend()
obj.deletemid()
obj.display()
