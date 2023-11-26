#!/usr/bin/python3
import random
import time


def get_level() -> int:
    while True:
        level: str = input("Level (1-3): ")
        if level in {"1", "2", "3"}:
            return int(level)


def generate_integer(level) -> list[list[int], list[int]]:
    return [[random.randint(10 ** (level - 1), (10 ** level) - 1) for _ in range(10)] for _ in range(2)]


def main() -> None:
    mistakes: int = 0
    x, y = generate_integer(get_level())

    start_time = time.time()
    for i in range(10):
        while True:
            try:
                user_result: int = int(input(f"{x[i]} + {y[i]} = "))
            except ValueError:
                print("Mauvais input, un nombre est attendu.")
                continue
            break
        if user_result != x[i] + y[i]:
            mistakes += 1
            print("Mauvais que tu es !!!")
            print(f"{x[i]} + {y[i]} = {x[i] + y[i]}")
    needed_time = time.time() - start_time
    print(f"{max(0, (10 - mistakes))}/10")
    if needed_time < 60:
        print(f"Tu as pris {round(time.time() - start_time)} secondes.")
    else:
        print(f"Tu as pris {needed_time // 60} min(s) et {needed_time % 60} secondes.")




if __name__ == "__main__":
    main()
