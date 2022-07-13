


from calendar import c
from math import gcd
from turtle import right
from unittest.util import sorted_list_difference

from pkg_resources import declare_namespace

class Functions():
    def __init__(self,top,den):
        self.top = top 
        self.den = den 
    
    def __str__ (self):
        return str(self.top) + "/" + str(self.den)
    
    def gcd(m,n):
        while m%n != 0:
            old_m = m
            old_n = n
            m = old_n
            n= old_m % old_n
        return n 
    

    def __add__ (self,otherfunction):
        newnum = self.top * otherfunction.den + self.den * otherfunction.top 
        nowden = self.den * otherfunction.den
        common =match.gcd(newnum,nowden)
        return Functions (newnum//common,nowden//common )
    def __eq__(self, otherfunction):
        fristnum= self.top * self.den
        secondunm = otherfunction.top * otherfunction.den
        return fristnum == secondunm
f1 = Functions(1,2)
f2 = Functions(1,8)

f3 = f1 +f2 
print(f1 == f2)
print(f3)