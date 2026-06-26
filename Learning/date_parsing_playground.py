"""
Topic:
    Datetime Parsing & Formatting

Purpose:
    Learn how to parse strings into dates and format dates as strings.

Things to Learn:
    - datetime.strptime()
    - datetime.strftime()
    - Accessing year, month, day
    - Current date and time
"""

from datetime import datetime


def main():

    print("=== Current Date & Time ===")
    print(datetime.now())
    print()

    print("=== Parsing Dates ===")

    date_string = "1886-12-11"

    parsed_date = datetime.strptime(date_string, "%Y-%m-%d")

    print(parsed_date)
    print()

    print("=== Accessing Components ===")

    print(f"Year: {parsed_date.year}")
    print(f"Month: {parsed_date.month}")
    print(f"Day: {parsed_date.day}")
    print()

    print("=== Formatting Dates ===")

    print(f"Formatted Date: {parsed_date.strftime('%d/%m/%Y')}")
    print(f"Formatted Date: {parsed_date.strftime('%B %d, %Y')}")
    print(f"Formatted Date: {parsed_date.strftime('%d %b. %Y')}")


if __name__ == "__main__":
    main()