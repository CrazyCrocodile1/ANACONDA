from collections import deque

def fibonacci_queue(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_queue = deque([0, 1])

    for i in range(2, n + 1):
        fib_queue.popleft()
        fib_queue.append(fib_queue[0] + fib_queue[1])

    return fib_queue[-1]

result = fibonacci_queue(10)
print("F(10) =", result)
