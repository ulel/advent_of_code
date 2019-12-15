"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a
password. The Elves had written the password on a sticky note, but someone
threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever
        increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet
these criteria?

Your puzzle input is 183564-657474.
"""

start = 183564
stop = 657474


def is_valid_password(password: int) -> bool:
    password_string = str(password)

    previous_digit = int(password_string[0])

    found_pair = False

    for digit in password_string[1:]:
        digit = int(digit)

        if digit == previous_digit:
            found_pair = True

        if digit < previous_digit:
            return False

        previous_digit = digit

    return found_pair


def main():
    number_of_valid_in_range = len(
        [password for password in range(start, stop + 1) if is_valid_password(password)]
    )
    print(f"part 1: {number_of_valid_in_range}")


if __name__ == "__main__":
    main()
