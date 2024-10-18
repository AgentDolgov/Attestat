class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real*other.real + self.imag*other.imag)/denom
        imag = (self.imag*other.real - self.real*other.imag)/denom
        return ComplexNumber(real, imag)