"""Fibonacci - the Grand Line crew grows like the sequence."""

def fibonacci(count: int) -> list[int]:
    seq = []
    a, b = 0, 1
    for _ in range(count):
        seq.append(a)
        a, b = b, a + b
    return seq

if __name__ == "__main__":
    n = int(input("How many Straw Hat members to count? "))
    print(fibonacci(n))
