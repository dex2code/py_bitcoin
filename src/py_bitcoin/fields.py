class FieldElement:

    def __init__(self, num, prime) -> None:
        if (num < 0) or (num >= prime):
            raise ValueError(f"Num '{num}' not in field range '0, ..., {prime - 1}'")
        
        self.num   = num
        self.prime = prime


    def __repr__(self) -> str:
        return f"FieldElement_{self.prime} ({self.num})"
    

    def __eq__(self, __value) -> bool:
        if __value is None:
            return False
        
        return (self.num == __value.num) and (self.prime == __value.prime)
    
    
    def __ne__(self, __value) -> bool:
        if __value is None:
            return True
        
        return not (self == __value)
    

    def __add__(self, __value) -> object:
        if self.prime != __value.prime:
            raise TypeError(f"self.prime '{self.prime}' is not equal to __value.prime '{__value.prime}'")
        
        new_num = (self.num + __value.num) % self.prime
        return self.__class__(num=new_num, prime=self.prime)


    def __radd__(self, __value) -> object:
        new_num = (self.num + __value) % self.prime
        return self.__class__(num=new_num, prime=self.prime)


    def __sub__(self, __value) -> object:
        if self.prime != __value.prime:
            raise TypeError(f"self.prime '{self.prime}' is not equal to __value.prime '{__value.prime}'")
        
        new_num = (self.num - __value.num) % self.prime
        return self.__class__(num=new_num, prime=self.prime)
    

    def __mul__(self, __value) -> object:
        if self.prime != __value.prime:
            raise TypeError(f"self.prime '{self.prime}' is not equal to __value.prime '{__value.prime}'")

        new_num = (self.num * __value.num) % self.prime
        return self.__class__(num=new_num, prime=self.prime)


    def __rmul__(self, __value) -> object:
        new_num = (self.num * __value) % self.prime
        return self.__class__(num=new_num, prime=self.prime)


    def __truediv__(self, __value) -> object:
        if self.prime != __value.prime:
            raise TypeError(f"self.prime '{self.prime}' is not equal to __value.prime '{__value.prime}'")
        
        if __value.num == 0:
            raise ZeroDivisionError

        new_num = (self.num * pow(base=__value.num, exp=self.prime-2, mod=self.prime)) % self.prime
        return self.__class__(num=new_num, prime=self.prime)     
    

    def __pow__(self, __value) -> object:
        __value = __value % (self.prime - 1)
        new_num = pow(base=self.num, exp=__value, mod=self.prime)
        return self.__class__(num=new_num, prime=self.prime)


from . import S256_PRIME


class S256_Field(FieldElement):

    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=S256_PRIME)


if __name__ == "__main__":
    pass