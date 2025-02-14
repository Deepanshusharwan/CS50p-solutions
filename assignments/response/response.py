from validator_collection import validators, errors
import sys
get_email = input("What's your email address? ")
if get_email.count("@") != 1 or "." not in get_email.split("@")[1]:
    print("Invalid")
    sys.exit(0)

try:
    valid_email = validators.email(get_email)
    print("Valid")
except (errors.EmptyValueError, errors.InvalidEmailError):
    print("Invalid")
    sys.exit(0)
