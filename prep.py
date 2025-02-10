# file2.py - Largest of Three Numbers

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    largest = find_largest(num1, num2, num3)
    print(f"The largest number is {largest}.")
    print("This is the first commit in this file")

def prep_function():
    print("This is the second Python file.")
