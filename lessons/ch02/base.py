class Point:

    def __init__(self, x, y, a, b) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        if (self.x is None) and (self.y is None):
            return
        
        if pow(y, 2) != pow(x, 3) + (a * x) + b:
            raise ValueError(f"Point ({x}, {y}) is not on the curve 'x**3 + {a}x + {b}'")


    def __repr__(self) -> str:
        if (self.x is None) and (self.y is None):
            return f"Infinity Point on curve 'x**3 + {self.a}x + {self.b}'"

        return f"Point ({self.x}, {self.y}) on curve 'x**3 + {self.a}x + {self.b}'"


    def __eq__(self, __value: object) -> bool:
        return (self.x == __value.x) and (self.y == __value.y) and (self.a == __value.a) and (self.b == __value.b)


    def __ne__(self, __value: object) -> bool:
        return not (self == __value)
    

    def __add__(self, __value: object) -> object:
        if (self.a != __value.a) or (self.b != __value.b):
            raise TypeError(f"Given points ('{self}' and '{__value}') aren't on the same curve!")
        
        if (self.x is None) and (self.y is None): # I + A = A
            return __value
        
        if (__value.x is None) and (__value.y is None): # A + I = A
            return self
        
        if self.x == __value.x: # Bot points are on the same X
            if self.y == __value.y:
                if (self.y == 0) and (__value.y == 0): # Both poins have Y == 0
                    return self.__class__(x=None, y=None, a=self.a, b=self.b)
                else: # A + A = B
                    s = (3 * pow(self.x, 2) + self.a) / (2 * self.y)
            else: # A + (-A) = I
                return self.__class__(x=None, y=None, a=self.a, b=self.b)
        else: # A + B = C
            s = (__value.y - self.y) / (__value.x - self.x)

        new_x = pow(s, 2) - self.x - __value.x
        new_y = s * (self.x - new_x) - self.y
        return self.__class__(x=new_x, y=new_y, a=self.a, b=self.b)
