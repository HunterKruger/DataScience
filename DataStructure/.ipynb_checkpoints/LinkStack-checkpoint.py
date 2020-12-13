from LinkList import Node

class StackOverFlowError(ValueError):
    pass

class LinkStack: # 基于链表实现
    
    def __init__(self):
        self._top = None 
        
    def is_empty(self):
        return self._top == None 
    
    def push(self, elem):
        self._top = Node(elem, self._top)
        
    def pop(self):
        if self._top is None:
            raise StackOverFlowError('in LinkStack pop()')
        p = self._top
        self._top = p.next
        return p.element
    
    def top(self):
        if self._top is None:
            raise StackOverFlowError('in LinkStack top()')
        return self._top.element