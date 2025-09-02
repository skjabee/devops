import sys

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <choice: add|sub|mul|div> <num1> <num2>")
        sys.exit(1)

    choice, num1, num2 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])

    if choice == "add":
        print(add(num1, num2))
    elif choice == "sub":
        print(subtract(num1, num2))
    elif choice == "mul":
        print(multiply(num1, num2))
    elif choice == "div":
        print(divide(num1, num2))
    else:
        print("Invalid choice")

