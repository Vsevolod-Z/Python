class Fraction(object):

   def __init__(self, num, den):
       self.__num = num #7
       self.__den = den #2
       self.reduce()


   def __str__(self):
       return "%d/%d" % (self.__num, self.__den)

   def reduce(self):
       g = Fraction.gcd(self.__num, self.__den)
       self.__num /= g
       self.__den /= g


   @staticmethod
   def gcd(n, m):
       if m == 0:
           return n
       else:
           return Fraction.gcd(m, n % m)
       
   def __neg__(self):
       return Fraction(-self.__num, self.__den)
   
   def __invert__(self):
       return Fraction(self.__den, self.__num)
   
   def __pow__(self, pow, modulo = None):
       return Fraction(self.__num ** pow, self.__den ** pow)
   
   def __float__(self):         
       return self.__num / self.__den
   
   def __int__(self):
       return int(self.__num / self.__den)
   






