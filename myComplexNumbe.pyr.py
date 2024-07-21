class myComplexNumber:
    def __init__(self, real = 0, imag = 0):
        print("myComplexNumber constructor executing...")
        self.real_part = real
        self.imag_part = imag

    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.imag_part))


cmplx1 = myComplexNumber(40, 50)
cmplx1.newAttribute = 20;
cmplx1.displayComplex()
# del cmplx1.newAttribute
# print(cmplx1.newAttribute)
print(cmplx1)
