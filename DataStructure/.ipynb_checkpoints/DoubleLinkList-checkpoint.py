from LinkList2 import LinkList2
from LinkList import Node, LinkListUnderflow

class DNode(Node):
    
    def __init__(self, element, prev = None, next_ = None):
        Node.__init__(self,element,next_)
        self.prev = prev
        
        
        
class DoubleLinkList(LinkList2):  # 带有首、尾节点引用的双链表
    
    def __init__(self):
        LinkList2.__init__(self)
        
    def prepend(self,element):
        p = DNode(element, None, self._head)
        if self._head is None:  #空表
            self._rear = p
        else:
            p.next.prev = p
        self._head = p
    
    def append(self, element):
        p = DNode(element, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p
    
    def pop(self):  # 表头删除
        if self._head is None:
            raise LinkListUnderflow('in pop DoubleLinkList')
        e = self._head.element
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkListUnderflow('in pop DoubleLinkList')
        e = self._rear.element
        self._rear = self._rear.prev
        if self._rear is None: # pop后表为空
            self._head = None
        else:
            self._rear.next = None
        return e