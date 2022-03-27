import re

postcode_regex = re.compile(
    "([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")


def two_chars(string):
    return len(string) >= 2


def six_digit_number(string):
    return string.isnumeric() and len(string) == 6


def valid_postcode(string):
    return 6 < len(string) < 9 and postcode_regex.match(string)


def validateInput(first_name, last_name, id, post_code):
    if not first_name:
        return "You must enter a first name."

    if not two_chars(first_name):
        return f'"{first_name}" is too short for a first name.'

    if not last_name:
        return "You must enter a last name."

    if not two_chars(last_name):
        return f'"{last_name}" is too short for a last name.'

    if not six_digit_number(id):
        return "The student ID must be numeric and six digits long."

    if not valid_postcode(post_code):
        return f'"{post_code}" is not a valid postcode.'

    return "There were no errors found."


first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
studentId = input("Enter student ID: ")
post_code = input("Enter post code: ")

print(f"\n{validateInput(first_name, last_name, studentId, post_code)}")
