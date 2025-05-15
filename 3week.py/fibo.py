def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 예: 0부터 9까지 피보나치 수 출력
for i in range(10):
    print(fibonacci_recursive(i), end=' ')
