### GLobal var ###
BALANCE = 1
HEIGHT = 0

class AVL_Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    ### Insertion ###
    def insert(self, val):
        if not self._value:
            self._value = AVL_Node(val)
        return self.insert_rec(val)[0]

    def insert_rec(self, val):
        height = self.height_balance(HEIGHT)
        root = self

        if val < self._value:
            if self._left:
                self._left = self._left.insert(val)
            else:
                if not self._right:
                    height += 1
                self._left = AVL_Node(val)

        if val > self._value:
            if self._right:
                self._right = self._right.insert(val)
            else:
                if not self._right:
                    height += 1
                self._right = AVL_Node(val)
        
        height = self.height_balance(HEIGHT)
        self.height_balance(BALANCE)
        return root, height

    ### Height & Balance ###
    def height_balance(self, param):
        right_height = 0
        if self._right:
            right_height = self._right.height_balance(HEIGHT)
        left_height = 0
        if self._left:
            left_height = self._left.height_balance(HEIGHT)
        if param == HEIGHT:
            return 1 + max(left_height, right_height)
        if param == BALANCE:
            self._balance = left_height - right_height
        if not param:
            print("ERR -height_balance- param is missing")


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


    # def insert(self, val) -> 'AVL_Node': # insertion val
    #     if self is None:
    #         h = 1
    #         return (self, h)
    #     if val <= self._value:
    #         (self._left, h) = self.insert(val)
    #     else:
    #         (self._right, h) = self.insert(val)
    #     return self
        # if self._balance + h == 2:

        
        
        
    # def rot_right(self):
    #     root: 'AVL_Node' = self._left
    #     if self._left:
    #         self._left = root._right
    #     root._right = self


    # def rot_left(self):
    #     root: 'AVL_Node' = self._right
    #     if self._right:
    #         self._right = root._left
    #     root._left = self  

        
    
        

        # if not self:
        #     return AVL_Node(val)
        # elif val < self._value:
        #     self._left = self._left.insert(val)
        # else:
        #     self._right = self._right.insert(val)

    
        # self.height += 1

        # balance = self._balance

        # if balance > 1 and val < self._left._value:
        #     return self.turn_right(self)

        # elif balance < -1 and val > self._right._value:
        #     return self.turn_left(self)

        # elif balance > 1 and val > self._left.value:
        #     self._left = self.turn_left(self._left)
        #     return self.turn_right(self)

        # elif balance < 1 and val < self._right.value:
        #     self._right = self.turn_right(self._right)
        #     return self.turn_left(self)
    
    # def turn_right(self, z):
    #     y = self.z._left
	# 	T3 = y._right

	# 	y.r = z
	# 	z.l = T3

	# 	z.h = 1 + max(self.getHeight(z.l),
	# 					self.getHeight(z.r))
	# 	y.h = 1 + max(self.getHeight(y.l),
	# 					self.getHeight(y.r))

	# 	return y

    # def turn_left(self, z):
        
	# 	y = self.z.r
	# 	T2 = y.l

	# 	y.l = z
	# 	z.r = T2

	# 	z.h = 1 + max(self.getHeight(z.l),
	# 					self.getHeight(z.r))
	# 	y.h = 1 + max(self.getHeight(y.l),
	# 					self.getHeight(y.r))

	# 	return y
