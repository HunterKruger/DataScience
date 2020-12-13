from LinkList import Node,LinkListUnderflow

class LinkList3:  # 循环单链表
    
    def __init__(self):
        self._rear = None
    
    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem):     #链表头加一个节点
        p = Node(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
        
            
    def pop(self): #链表头删除节点
        if self._rear is None:
            raise LinkListUnderflow('in pop of LinkList3')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next      
        return p.element
    
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next
    
    def print_all(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.element)
            if p is self._rear:
                break
            p = p.next
        