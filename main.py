# file1.py - Even or Odd Checker

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(f"The number {number} is {result}.")
