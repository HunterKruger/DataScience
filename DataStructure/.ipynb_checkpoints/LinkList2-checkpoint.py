from LinkList import LinkList,Node,LinkListUnderflow
import random

class LinkList2(LinkList): # 单链表变种，表对象加入一个表尾节点引用域
    
    def __init__(self):
        LinkList.__init__(self)
        self._rear = None    
     
    
    def prepend(self, element):
        if self._rear is None: #是空表
            self._head = Node(element, self._head)
            self._rear = self._head
        else:
            self._head= Node(element, self._head)
     
    
    def append(self, element):
        if self._head is None:
            self._head = Node(element,self._head)
            self._rear = self._head
        else:
            self._rear.next = Node(element)
            self._rear = self._rear.next
    
    
    def pop_last(self):
        
        if self._head is None:
            raise LinkListUnderflow('in pop_last')
        p = self._head
        
        if p.next is None: #表中只有一个元素
            e = p.element
            self._head = None
            return e
        
        while p.next.next is not None:
            p = p.next
        e = p.next.element
        p.next=None
        self._rear = p
            
        return e
 
        
    