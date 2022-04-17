class AVL_Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    def insert(self, val) -> 'AVL_Node': # insertion val
        if val < self._value:
            if self._left is None:
                return self
            root = self._left
            root.insert(val)
        else:
            if self._right is None:
                return self
            root = self._right
            root.insert(val)

    def height(self):
        right_height = 0
        if self._right:
            right_height = self._right.height()
        left_height = 0
        if self._left:
            left_height = self._left.height()
        return max(left_height, right_height) + 1


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
