# The Fibonacci sequence is an infinite series of numbers where each number is the sum of the two preceding ones
# The sequence starts with 0 and 1, and the next numbers in the sequence are 1, 2, 3, 5, 8, 13, and so on.
# The Fibonacci sequence can be defined using the following recursive formula:
# F(n) = F(n-1) + F(n-2)
# with the base cases F(0) = 0 and F(1) = 1.  




def fib(num):
    a = int(input('Enter first variable of the sequence: '))
    b = int(input('Enter second variable of the sequence: '))
    while a < num:
        print(a, end=" ")
        a, b = b , a+b
    print()
fib(200)