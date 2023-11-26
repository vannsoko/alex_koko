#!/usr/bin/python3
import random
import time


def get_level() -> int:
    """
        Returns the user-given level.

        :return: The level as an integer, 1, 2, or 3.
    """
    while True:
        level: str = input("Level (1-3): ")
        if level in {"1", "2", "3"}:
            return int(level)


def generate_integer(level: int) -> list[list[int], list[int]]:
    """
        Generates two lists of random integers based on the given level.

        :param level: The level of the generated integers.
        :return: A list containing two lists of integers.
    """
    return [[random.randint(10 ** (level - 1), (10 ** level) - 1) for _ in range(10)] for _ in range(2)]


def format_time(seconds: int | float) -> str:
    """
      Formats the given time in seconds into a string representation.

      :param seconds: The time in seconds.
      :return: A string representation of the formatted time.
    """
    mins, secs = divmod(seconds, 60)
    return f"{int(mins)} min(s) et {int(secs)} secondes" if mins else f"{int(secs)} secondes"


def main() -> None:
    """
        Runs the main logic of the basic math professor program.

        :return: None
    """
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
    print(f"Tu as pris {format_time(needed_time)}.")


if __name__ == "__main__":
    main()
