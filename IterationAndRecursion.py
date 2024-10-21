print("iterative and recursive functionality")
def iterative_factorial(n):
    result =1
    for i in range(1, n + 1):
        result *=i
    return result

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    
numbers = [0,5,10,25,50,100]

for _ in range(5):
    print("Factroial results using the iterative function:")
    for num in numbers:
        print(f"Iterative Factroial of {num}:{iterative_factorial(num)}")
    print("\nFactorial reults using a recursive function:")
    for num in numbers:
        print(f"Recursive Factorial of {num}:{recursive_factorial(num)}")
        
print("\n" + "="*50 + "\n")