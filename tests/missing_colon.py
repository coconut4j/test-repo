#!/usr/bin/env python3


def division(a: float, b: float) -> float:
    if b == 0:
        return 'Error: Division by zero'
    return a/b


if __name__ == "__main__":
    print(division(123, 15))

