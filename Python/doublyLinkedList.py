class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def push(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = NewNode
        NewNode.prev = cur

    def insertAtBeginning(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        NewNode.next = self.head
        self.head.prev = NewNode
        self.head = NewNode
        
    def insertAfter(self,middle_node,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            print("Linked List is Empty")
            return
        cur = self.head
        while cur:
            if cur.data == middle_node:
                temp = cur.next # for cur.next.prev to set NewNode
                NewNode.next = cur.next
                NewNode.prev = cur
                cur.next = NewNode
                temp.prev = NewNode # bcz cur is overwrite by NewNode
                return
            cur = cur.next
    
    def removeNode(self,data):
        if self.head is None:
            print("Linked List is Empty..")
            return
        cur = self.head
        if cur.data == data:
            self.head = cur.next
            cur = None
            return

        while cur:
            if cur.data == data:
                if (cur.next != None):
                    cur.next.prev = cur.prev

                if (cur.prev != None):
                    cur.prev.next = cur.next
                return
            cur = cur.next

    def bubbleSort(self):
        cur = self.head
        idx = None
        if self.head == None:
            return
        else:
            while cur:
                idx = cur.next
                while idx:
                    if cur.data > idx.data:
                        cur.data, idx.data = idx.data, cur.data
                    idx = idx.next

                cur = cur.next
    # time : O(n*n)

    def insertionSort(self,head_ref):
        sortedLL = None
        cur = head_ref
        while cur:
            nxt = cur.next
            cur.prev = cur.next = None
            sortedLL = self.sortedInsert(sortedLL,cur)
            cur = nxt
        head_ref = sortedLL
        return head_ref

    def sortedInsert(self,head_ref, NewNode):
        if head_ref == None:
            head_ref = NewNode 
        elif head_ref.data >= NewNode.data:
            NewNode.next = head_ref
            # head_ref.prev = NewNode
            NewNode.next.prev = NewNode
            head_ref = NewNode
        else:
            cur = head_ref
            while cur.next != None and cur.next.data < NewNode.data:
                cur = cur.next
            NewNode.next = cur.next
            if cur.next != None:
                cur.next.prev = NewNode
            cur.next =  NewNode
            NewNode.prev = cur
        return head_ref

    def sortedMerge(self,a,b):
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a        
            result.next = self.sortedMerge(a.next,b)
            result.next.prev = a
            result.prev = None
        else:
            result = b
            result.next = self.sortedMerge(a,b.next)
            result.next.prev = b
            result.prev = None
        return result
    def mergeSort(self,h):
        if h is None or h.next is None:
            return h
        middle = self.getMiddle(h)
        nextToMiddle = middle.next
        
        # it divides
        middle.next = None
        nextToMiddle.prev = None

        left = self.mergeSort(h)
        right = self.mergeSort(nextToMiddle)


        sortedList = self.sortedMerge(left,right)
        return sortedList


    def getMiddle(self,head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def partition(self, start, end):
        pivot = start
        cur = start
        while (cur != None and cur != end):
            if (cur.data < end.data):
                pivot = start
                start.data, cur.data = cur.data,start.data
                start = start.next
            cur = cur.next
        if cur is None:
            cur  = start
        start.data,end.data = end.data, start.data
        return pivot

    def quickSort(self, start, end):
        if start == end:
            return
        pivot = self.partition(start, end)
        if pivot != None:
            self.quickSort(pivot.next, end)
            self.quickSort(start, pivot)



    def printLL(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        cur = self.head
        print("\nDisplaing Elements of Linked List: ")
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

dll = DLinkedList()
#dll.push(1)
#dll.push(2)
#dll.push(12)
#dll.push(9)
#dll.push(4)
#dll.printLL()
#dll.insertAtBeginning(3)  #while using this(one time) insertion sort after sorting remove two elements after "3"
#dll.insertAtBeginning(1) # using it second time didn't  remove elements (-__-)
#dll.printLL()
#dll.insertAfter(2,8)
#dll.insertAfter(8,11)
#dll.printLL()
#dll.removeNode(8)
#dll.removeNode(11)
#dll.printLL()
# dll.bubbleSort()
# dll.printLL()
print()
# dll.insertionSort(dll.head)
# dll.head = dll.mergeSort(dll.head)
# dll.printLL()
#last = dll.head
#while last.next:
 #   last = last.next
#dll.quickSort(dll.head,last)
#dll.printLL()
