from controller import Calculator
import sys

from model import ComplexNumber

def get_complex_number():
    real = float(input("Enter the real part of the complex number: "))
    imag = float(input("Enter the imaginary part of the complex number: "))
    return ComplexNumber(real, imag)

def main():
    calculator = Calculator()

    print("Choose operation:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")

    choice = int(input("Enter choice: "))

    num1 = get_complex_number()
    num2 = get_complex_number()

    if choice == 1:
        result = calculator.add(num1, num2)
        print(f"Result: {result.real} + {result.imag}i")
    elif choice == 2:
        result = calculator.multiply(num1, num2)
        print(f"Result: {result.real} + {result.imag}i")
    elif choice == 3:
        result = calculator.divide(num1, num2)
        print(f"Result: {result.real} + {result.imag}i")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()