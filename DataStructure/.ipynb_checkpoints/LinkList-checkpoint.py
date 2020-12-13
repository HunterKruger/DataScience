class Node:
    def __init__(self,element,next_ = None):
        self.element = element
        self.next = next_   # 下划线避免与关键字重名
        
class LinkListUnderflow(ValueError):
    pass
    
class LinkList:
    
    def __init__(self):
        self._head = None    # 表头指针
        # 前下划线 意味着Python社区一致认为它应该是什么意思，但程序的行为不受影响。
    
    
    def is_empty(self):
        return self._head is None
    
    
    def delete_list(self):
        self._head = None
    
    
    def prepend(self, elem):     #链表头加一个节点
        self._head = Node(elem, self._head)
        
        
    def pop(self): #链表头删除节点
        if self._head is None:
            raise LinkListUnderflow('in pop')
        e = self._head.element
        self._head = self._head.next
        return e
    
    
    def append(self, elem):
        if self._head is None:
            self.element = Node(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Node(elem)
            
            
    def pop_last(self):
        
        if self.is_empty():
            raise LinkListUnderFlow('in link list pop last')
        p = self._head
        
        if p.next is None:
            e = p.element
            p.next = None
            return e
        
        while p.next.next is not None:
            p = p.next
        e = p.next.element
        p.next = None
        return e
    

    def for_each(self,proc):  # 遍历函数， proc 为函数名， 可以是print, pop ...
        p = self._head
        while p is not None:
            proc(p.element)
            p = p.next
            
    
    def elements(self):  # 定义生成器函数 （迭代器）
        p = self._head
        while p is not None:
            yield p.element
            p = p.next
            
            
    def counts(self):
        p = self._head
        count = 0
        while p is not None:
            count+=1
            p = p.next
        return count
    
    
    def find(self, target):
        p = self._head
        while p is not None:
            if target == p.element:
                return True
            p = p.next
        return False
    
    
    def print_all(self):
        p = self._head
        while p is not None:
            print(p.element, end = '')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')
        
        
    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.element <= rem.element:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p 
            
    def reverse(self): # double pointer
        pre = None  # previous
        cur = self._head  # current
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        self._head = pre