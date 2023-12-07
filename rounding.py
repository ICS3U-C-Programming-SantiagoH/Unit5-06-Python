#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Dec 6, 2023
# This program will ask for a decimal
# and a number of decimal places to round to
# and it will display the new rounded number


def round_decimal(decimal, num_place):
    # round decimal number to user's preference
    decimal[0] = decimal[0] * 10**num_place + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / 10**num_place


def main():
    # get decimal and places and display message to user
    print("This program will ask for a decimal")
    print("and a number of decimal places to round to")
    print("and it will display the new rounded number")

    user_decimal_float = [0]
    user_decimal_str = input("Please enter your decimal: ")
    user_places_str = input("Please enter your decimal places to round the number: ")

    # convert decimal and places
    try:
        user_decimal_float[0] = float(user_decimal_str)
        user_places_int = int(user_places_str)

        # Call function and store rounded number
        round_decimal(user_decimal_float, user_places_int)

        # display new rounded number to user
        print(f"The rounded number is {user_decimal_float[0]}")

    # catch invalid input
    except Exception:
        print(
            f"{user_decimal_str} and {user_places_str} are not a valid number and/or decimal place"
        )


if __name__ == "__main__":
    main()
