### GLobal var ###
NB_ROT = 0

### Global func ###
def reset_nb_rot():
    global NB_ROT
    NB_ROT = 0

def increment_nb_rot():
    global NB_ROT
    NB_ROT += 1

### CLass AVL_Node ###
class AVL_Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    def height(self):
        if not self:
            return 0
        r_node = 0
        l_node = 0
        if self._right:
            r_node = self._right.height()
        if self._left:
            l_node = self._left.height()
        return 1 + max(r_node, l_node)

    def balance(self):
        if not self:
            return 0
        r_node = 0
        l_node = 0
        if self._right:
            r_node = self._right.height()
        if self._left:
            l_node = self._left.height()
        return l_node - r_node


    ### Insertion ###
    def insert(self, val):
        if not val:
            return False
        root = self.insert_rec(val)[0]
        return root

    def insert_rec(self, val):
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

    def leftleft(self):
        return self.rot_right()
    
    def leftright(self):
        self._left = self._left.rot_left()
        return self.leftleft()

    def rightright(self):
        return self.rot_left()
    
    def rightleft(self):
        self._right = self._right.rot_right()
        return self.rightright()

    def rot_cases(self):
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
        

    def rot_left(self):
        node = self._right
        self._right = node._left
        node._left = self
        node._balance = 0
        self._balance = self.balance()
        increment_nb_rot()
        return node


    def rot_right(self):
        node = self._left
        self._left = node._right
        node._right = self
        node._balance = 0
        self._balance = self.balance()
        increment_nb_rot()
        return node


    ### Print Tree ###
    def printTree(self):
        print("")
        self.printTree_rec()

    def printTree_rec(self):
        if self._left:
            self._left.printTree_rec()
        print(self._value)
        if self._right:
            self._right.printTree_rec()
            self._right.printTree_rec()