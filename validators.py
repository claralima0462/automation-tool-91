import re

# Validates email format using regex

def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

# Validates a positive integer

def validate_positive_integer(value):
    try:
        ivalue = int(value)
        return ivalue >= 0
    except ValueError:
        return False

# Validates if the input is a non-empty string

def validate_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())

# Validates the length of a string

def validate_string_length(value, min_length=1, max_length=255):
    if not isinstance(value, str):
        return False
    length = len(value)
    return min_length <= length <= max_length

# Consolidate validation checks

def validate_user_input(email, age, name):
    return (validate_email(email) and
            validate_positive_integer(age) and
            validate_non_empty_string(name))

if __name__ == '__main__':
    print(validate_user_input('test@example.com', '25', 'John Doe'))
    print(validate_user_input('invalid-email', '25', ''))
