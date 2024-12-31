class complexnumbers():
    def __init__(self , real , imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self , other):
            return complexnumbers(self.real + other.real , self.imaginary + other.imaginary)
    def __sub__(self , other):
            return complexnumbers(self.real - other.real , self.imaginary - other.imaginary)
    def __mul__(self , other):
            real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
            imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
            return complexnumbers(real_part , imaginary_part)
    def __str__(self):
            return f"{self.real} + {self.imaginary}i"

if __name__ == "__main__":       
    c1 = complexnumbers(2,3)
    c2 = complexnumbers(1,4)
    result__add = c1+c2
    print(f"Addition : {result__add}")
    result__sub = c1-c2
    print(f"Subtraction : {result__sub}")
    result__mul = c1*c2
    print(f"Multiplication : {result__mul}")