# This program calculates a factorial
# WITH recursion

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        x = factorial_recursive(n - 1)
        print(n, "*", x, "=", n * x)
        return n * x


print("I can calculate a factorial!")
user_input = input("Enter a number:")
n = int(user_input)
answer = factorial_recursive(n)
print(answer)