### GLobal var ###
NB_ROT = 0

### Global func ###
def reset_nb_rot():
    global NB_ROT
    NB_ROT = 0

######################
### CLass AVL_Node ###
######################

class AVL_Node:
    def __init__(self, value):
        self._value: 'int' = value
        self._left: 'AVL_Node' = None
        self._right: 'AVL_Node' = None
        self._balance : 'int' = 0

    def height(self)->'int':
        if not self:
            return 0
        r_node: 'int' = 0
        l_node: 'int' = 0
        if self._right:
            r_node = self._right.height()
        if self._left:
            l_node = self._left.height()
        return 1 + max(r_node, l_node)

    def balance(self)->'int':
        if not self:
            return 0
        r_node: 'int' = 0
        l_node: 'int' = 0
        if self._right:
            r_node = self._right.height()
        if self._left:
            l_node = self._left.height()
        return l_node - r_node


    ######################
    ###    Insertion   ###
    ######################

    def insert(self, val)->'AVL_Node':
        if not val:
            return False
        root: 'AVL_Node' = self.insert_rec(val)[0]
        return root

    def insert_rec(self, val)->('AVL_Node', 'int'):
        if not self._value:
            self._value = AVL_Node(val)

        if val > self._value:
            if self._right:
                self._right = self._right.insert(val)
            else:
                self._right = AVL_Node(val)
        if val < self._value:
            if self._left:
                self._left = self._left.insert(val)
            else:
                self._left = AVL_Node(val)
        self._balance = self.balance()
        return self.rot_cases(), self.height()
    
    ### Rotations ###

    def leftleft(self)->'AVL_Node':
        return self.rot_right()
    
    def leftright(self)->'AVL_Node':
        self._left = self._left.rot_left()
        return self.leftleft()

    def rightright(self)->'AVL_Node':
        return self.rot_left()
    
    def rightleft(self)->'AVL_Node':
        self._right = self._right.rot_right()
        return self.rightright()

    def rot_cases(self)->'AVL_Node':
        if self._balance == 2:
            if self._left._left:
                return self.leftleft()
            if self._left._right:
                return self.leftright()
        if self._balance == -2:
            if self._right._right:
                return self.rightright()
            if self._right._left:
                return self.rightleft()
        return self
        

    def rot_left(self)->'AVL_Node':
        global NB_ROT
        node: 'AVL_Node' = self._right
        self._right = node._left
        node._left = self
        node._balance = 0
        self._balance = self.balance()
        NB_ROT += 1
        return node


    def rot_right(self)->'AVL_Node':
        global NB_ROT
        node: 'AVL_Node' = self._left
        self._left = node._right
        node._right = self
        node._balance = 0
        self._balance = self.balance()
        NB_ROT += 1
        return node

    
    ######################
    ###     Remove     ###
    ######################

    def delete(self, val)->'AVL_Node':
        if not val:
            return False
        root: 'AVL_Node' = self.delete_rec(val)[0]
        self._balance = self.balance()
        return root

    
    def delete_rec(self, val):
        if val > self._value:
            if self._right:
                self._right = self._right.delete(val)
        if val < self._value:
            if self._left:
                self._left = self._left.delete(val)
        if val == self._value:
            if not self._left:
                return self._right, self.height()
            if not self._right:
                return self._left, self.height()

        return self.rot_cases(), self.height()
        

    ######################
    ###     Print      ###
    ######################
    def printTree(self):
        print("")
        self.printTree_rec()

    def printTree_rec(self):
        if self._left:
            self._left.printTree_rec()
        print(self._value)
        if self._right:
            self._right.printTree_rec()
