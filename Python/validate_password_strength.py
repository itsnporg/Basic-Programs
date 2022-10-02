import re
def validate_password_strength(
    password_string, min_length=8, max_length=25,
    lower_case=True, upper_case=True, number=True,
    special_char=True, allowed_special_chars=list()
):
    """
    # Method to check if password is valid as per the required strength.


    Args:
        password_string (str): Password string to validate.
        min_length (int, optional): minimum no of required characters. Defaults to 8.
        max_length (int, optional): maximum no of required characters. Defaults to 25.
        lower_case (bool, optional): require lower case in password_string such as abc. Defaults to True.
        upper_case (bool, optional): require upper case in password_string such as ABC . Defaults to True.
        number (bool, optional): require number in password_string. Defaults to True.
        special_char (bool, optional): required special characters in password_string such as @,$,etc . Defaults to True.
        allowed_special_chars (str, optional): list of characters that are allowed for special characters in password_string. Defaults to empty list.

    Returns:
        (bool, list): if password is valid or not, list of messages with what is required.
    """

    # The password must contain lowercase, uppercase, digit and supported special characters.
    msgs = list()
    is_valid = True

    # Check for required length constrains
    if (len(password_string) < min_length or len(password_string) > max_length):
        is_valid = False
        msgs.append(f'Password LENGTH must be BETWEEN: {min_length} to {max_length} characters')

    # special_char_ascii = [ord(char) for char in ]
    if lower_case and (not re.match(r'\w*[a-z]\w*', password_string)):
        is_valid = False
        msgs.append("Must contain LOWER CASE letter")

    if upper_case and (not re.match(r'\w*[A-Z]\w*', password_string)):
        is_valid = False
        msgs.append("Must contain UPPER CASE letter")

    if number and (not re.search(r'\d', password_string)):
        is_valid = False
        msgs.append("Must contain NUMBER")

    # if not allowed_special_chars are passed from arguments then set default characters,.
    if not allowed_special_chars:
        # do not change the sequence as below
        allowed_special_chars = ['[', '@', '_', '!', '#', '$', '%', '^', '&',
                                    '*', '(', ')', '<', '>', '?', '/', '\\', ' | ', '}', '{', '~', ']', ]

    if special_char and (not (re.compile(''.join(allowed_special_chars))).search(password_string)):
        is_valid = False
        msgs.append("Must contain SPECIAL CHARACTER")

    return is_valid, msgs


# usage 

# >>> validate_password_strength("Hello@1234")
