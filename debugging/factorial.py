import sys

def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        return
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer")
        return
    
    print(factorial(n))

if __name__ == "__main__":
    main()

