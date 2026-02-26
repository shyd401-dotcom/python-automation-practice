#!/usr/bin/env python3
import sys

def is_even(n: int) -> bool:
    return n % 2 == 0


def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                n = int(arg)
                print(f"{n} is {'even' if is_even(n) else 'odd'}")
            except ValueError:
                print(f"'{arg}' is not an integer")
    else:
        try:
            n = int(input("Enter an integer: ").strip())
            print(f"{n} is {'even' if is_even(n) else 'odd'}")
        except Exception:
            print("Invalid input")


if __name__ == '__main__':
    main()
