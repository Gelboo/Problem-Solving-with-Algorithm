class Fraction:
    def __init__(self,top,bottom):
        if type(top) != int or type(bottom) != int:
            raise RuntimeError("Please use Integer values for Fraction inputs")
        common = self.gcd(top,bottom)
        self.num = top//common
        self.den = bottom//common


    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    def __eq__(self,other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num
    def __gt__(self,other):
        if self.den < other.den:
            return True
        elif self.den == other.den and self.num > other.den:
            return True
        else:
            return False
    def __lt__(self,other):
        if self.den > other.den:
            return True
        elif self.den == other.den and self.num < other.den:
            return True
        else:
            return False
    def __add__(self,other):
        new_num = (self.num*other.den)+(self.den*other.num)
        new_den = self.den * other.den
        #common = self.gcd(new_num,new_den)
        return Fraction(new_num,new_den)
    '''
     the difference between __add__ and __radd__
     if i use myobj+4 will work as myobj.__add__(4)
     but when use 4+myobj will work as (4).__add__myobj which will not work
     because the built-in object integer doesn't new my class
     here come __radd__ try (4).__radd__(myobject) if not worked (return ValueError)
     try from left to rigth (myobject)__radd__(4)
    '''
    def __radd__(self,other):
        new_num = (self.num*other.den)+(self.den*other.num)
        new_den = self.den * other.den
        #common = self.gcd(new_num,new_den)
        return Fraction(new_num,new_den)
    def __mul__(self,other):
        return Fraction(self.num*other.num,self.den*other.den)
    def __sub__(self,other):
        new_num = (self.num*other.den)-(self.den*other.num)
        new_den = self.den * other.den
        #common = self.gcd(new_num,new_den)
        return Fraction(new_num,new_den)
    def __div__(self,other):
        return Fraction(self.num/other.num,self.den/other.den)
    def __floordiv__(self,other):
        return Fraction(self.num//other.num,self.den//other.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    def gcd(self,m,n):
        while m%n != 0:
            new_m = n
            new_n = m%n
            m = new_m
            n = new_n
        return n


def test():
    myFraction = Fraction(15,10)
    yourFraction = Fraction(30,10)
    TestFraction = Fraction(1,3)
    # print("GCD= ",gcd(8,6))
    assert (myFraction.getNum()) == 3
    assert (myFraction.getDen()) == 2
    # assert (myFraction + yourFraction) == Fraction(9,2)
    assert (myFraction-yourFraction) == Fraction(-3,2)
    assert (myFraction*yourFraction) == Fraction(9,2)
    assert (myFraction/yourFraction) == Fraction(1,2)
    assert (myFraction//yourFraction) == Fraction(1,2)
    assert (myFraction > yourFraction) == False
    # print(Fraction(1,2)>Fraction(1,3))
    assert (myFraction < yourFraction) == True
    assert (myFraction == yourFraction) == False
test()
