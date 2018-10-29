import random 
 
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
 
    def __str__(self):
        return 'Node ['+str(self.value)+']'
 
class LinkedList:
    def __init__(self):
        self.first = None
        self.last  = None
        self.length = 0
 
    def add(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current
 
    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [ ' +str(current.value) +' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']\n'
        return 'LinkedList []'
 
    def BubbleSort(self):
       a = Node(0,None)
       b = Node(0,None)
       c = Node(0,None)
       e = Node(0,None)
       tmp = Node(0,None)
        
       while(e != self.first.next) :
        c = a = self.first
        b = a.next
 
        while a != e:
          if a and b:
            if a.value > b.value:
              if a == self.first:
                tmp = b.next
                b.next = a
                a.next = tmp
                self.first = b
                c = b
              else:
                tmp = b.next
                b.next = a
                a.next = tmp
                c.next = b
                c = b
            else:
              c = a
              a = a.next
            b = a.next
            if b == e:
              e = a
          else:
              e = a
               
     
L  = LinkedList()
 
for i in range ( 0, 10 ) : 
  L.add ( int ( random.uniform ( 0, 10 ) ) )
 
print L
L.BubbleSort()
print L