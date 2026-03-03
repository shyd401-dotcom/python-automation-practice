#!/usr/bin/env python3
import sys

def is_even(n: int) -> bool:
    return n % 2 == 0


def analyze_range(start: int, end: int) -> dict:
    """Return a summary of even/odd counts for the inclusive range.

    If `start` > `end` the range is still processed by swapping the values.
    The returned dictionary has the keys ``'even'`` and ``'odd'`` with
    integer counts.
    """
    # ensure the range works in either direction
    if start > end:
        start, end = end, start

    even_count = 0
    odd_count = 0
    for n in range(start, end + 1):
        if is_even(n):
            even_count += 1
        else:
            odd_count += 1
    return {"even": even_count, "odd": odd_count}


def main():
    # the program will operate in two modes:
    # 1. single integer arguments -> classify each number.
    # 2. a pair of integers separated by a dash (e.g. 3-8) -> analyze range.
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            # detect range notation
            if "-" in arg:
                parts = arg.split("-", 1)
                try:
                    start = int(parts[0])
                    end = int(parts[1])
                    summary = analyze_range(start, end)
                    print(f"Range {start} to {end}: {summary['even']} even, {summary['odd']} odd")
                except ValueError:
                    print(f"'{arg}' is not a valid range of integers")
            else:
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
