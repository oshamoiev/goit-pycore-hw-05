def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        value = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = value
        return value

    return fibonacci


def main():
    fibonacci_calculator = caching_fibonacci()
    print(fibonacci_calculator(10))
    print(fibonacci_calculator(15))


if __name__ == "__main__":
    main()