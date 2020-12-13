class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST: #二叉搜索树
    
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
                
    def preorder_trav(self, subtree):   # 先根遍历
        if subtree is not None:
            print(subtree.data, end=',')    # 递归函数里先处理根
            self.preorder_trav(subtree.left)   # 递归处理左子树
            self.preorder_trav(subtree.right)    # 递归处理右子树
            
    def midorder_trav(self, subtree):  # 中根遍历
        if subtree is not None:
            self.midorder_trav(subtree.left)
            print(subtree.data, end=',')
            self.midorder_trav(subtree.right)
    
    def lastorder_trav(self, subtree):  # 后根遍历
        if subtree is not None:
            self.lastorder_trav(subtree.left)
            self.lastorder_trav(subtree.right)
            print(subtree.data, end=',')
        
    def insert(self, subtree, val):  #递归实现
        if subtree is None:
            subtree = BSTNode(val)
        elif val < subtree.data:
            subtree.left = self.insert(subtree.left,val)
            subtree.left.parent = subtree
        elif val > subtree.data:
            subtree.right = self.insert(subtree.right,val)
            subtree.right.parent = subtree
        return subtree
    
    def insert_no_rec(self, val):
        p = self.root
        if p is None:
            self.root = BSTNode(val)
            return
        while True:
            if val<p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = BSTNode(val)
                    p.left.parent = p
                    return
            elif val>p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BSTNode(val)
                    p.right.parent = p
                    return
            else:
                return
                

    def find(self, subtree, val): #递归实现
        if not subtree:
            return None
        if val > subtree.data:
            return self.find(subtree.right, val)
        elif val < subtree.data:
            return self.find(subtree.left, val)
        else:
            return subtree
        
    def find_no_rec(self,val):
        p = self.root
        while True:
            if p is None:
                return None   
            elif p.data<val:
                p = p.right
            elif p.data>val:
                p=p.left
            else:
                return p
            
    def delete(self,val):
        if self.root is not None:
            node = self.find_no_rec(val)
            if node is None:
                return False
            if not node.left and not node.right:
                self.__delete_case_1(node)
            elif not node.right:
                self.__delete_case_2_1(node)
            elif not node.left:
                self.__delete_case_2_2(node)
            else: #两个孩子都有
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.data = min_node.data
                if min_node.right:
                    self.__delete_case_2_2(min_node)
                else:
                    self.__delete_case_1(min_node)        
        
    def __delete_case_1(self,node):
        # 情况1:删除的是叶子节点
        if not node.parent: #如果节点父亲为空
            self.root = None
        if node == node.parent.left:
            node.parent.left = None
        else: # node == node.parent.right
            node.parent.right = None
    
    def __delete_case_2_1(self,node):
        # 情况2.1: node只有一个左孩子
        if not node.parent: # is root
            self.root = node.left
            node.left.parent = None
        elif node == node.parent.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else: # node == node.parent.right
            node.parent.right = node.left
            node.left.parent = node.parent
    
    def __delete_case_2_2(self, node):
        # 情况2.2: node只有一个右孩子
        if not node.parent:
            self.root = node.right
        elif node == node.parent.left:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent
    
    
             
             
            
            