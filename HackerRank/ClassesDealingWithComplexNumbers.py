import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, no):
        return Complex(self.real + no.real,
                       self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real,
                       self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real, imaginary)

    def conj(self): # Complex Conjugate
        return Complex(self.real, -self.imaginary)

    def __truediv__(self, no):
        if no.imaginary == 0:
            return Complex(self.real / no.real,
                           self.imaginary / no.real)
        else:
            return ((self * no.conj()) / (no * no.conj())) #self = self.real+self.imaginary, no = no.real+no.imaginary

    def mod(self): # Defined as |z| = sqrt(Re**2 + Im**2)
        squared = (self.real**2 + self.imaginary**2)
        return Complex(math.sqrt(squared),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c) # Takes array c's 2 arguments for Complex() class.
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

################
# LOCAL
# f = open('data/input.txt', 'r')
#
# import math
#
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = float(real)
#         self.imaginary = float(imaginary)
#
#     def __add__(self, no):
#         return Complex(self.real + no.real,
#                        self.imaginary + no.imaginary)
#
#     def __sub__(self, no):
#         return Complex(self.real + no.real,
#                        self.imaginary + no.imaginary)
#
#     def __mul__(self, no):
#         real = (self.real * no.real) - (self.imaginary * no.imaginary)
#         imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
#         return Complex(real, imaginary)
#
#     def conj(self):
#         return Complex(self.real, -self.imaginary)
#
#     def __truediv__(self, no):
#         if no.imaginary == 0:
#             return Complex(self.real / no.real,
#                            self.imaginary / no.real)
#         else:
#             return ((self * no.conj()) / (no * no.conj())) #self = self.real+self.imaginary, no = no.real+no.imaginary
#
#     def mod(self):
#         squared = (self.real**2 + self.imaginary**2)
#         return Complex(math.sqrt(squared),0)
#
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result
#
#
# if __name__ == '__main__':
#     c = map(float, f.readline().split())
#     d = map(float, f.readline().split())
#     x = Complex(*c) # Takes array c's 2 arguments for Complex() class.
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')