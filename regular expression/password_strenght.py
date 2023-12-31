import re  # Import the regular expression library re

password_regex = re.compile(r"""(.){8,}""")  # Compile a regular expression that matches passwords of at least 8 characters


# Define a dictionary to store the regular expressions for each security stage
security_stages = {
    "lowercase letter": re.compile(r"""[a-z]+"""),  # Match one or more lowercase letters
    "uppercase letter": re.compile(r"""[A-Z]+"""),  # Match one or more uppercase letters
    "number": re.compile(r"""[0-9]+"""),  # Match one or more numbers
    "special character": re.compile(r"""[^a-zA-Z0-9]+"""),  # Match one or more special characters that are not letters or numbers
}


def validate_password(password):
    """
    Validate a password based on the defined security stages

    Args:
        password (str): The password to validate

    Returns:
        bool: True if the password passes all security stages, False otherwise

    Raises:
        ValueError: If the password is empty
    """
    if not password:
        raise ValueError("Password cannot be empty")

    failed_stage = ""  # Initialize a variable to store the name of the failed security stage, if any

    # Iterate through each security stage and check if the password matches the regular expression
    for stage, regex in security_stages.items():
        if not regex.search(password):
            failed_stage = stage
            break

    if failed_stage:
        # If the password fails at least one security stage, raise a ValueError with the failed stage
        raise ValueError(f"Password must contain at least one {failed_stage}")

    # If the password passes all security stages, return True
    return True


while True:
    try:
        text = input("Enter your password: ")
        password = password_regex.search(text).group()  # Extract the matched password from the input text
        validate_password(password)  # Validate the password
        print("Your password is secure!")
        break  # Break out of the while loop when the password is validated
    except ValueError as e:
        print(e)  # Print any error messages
        continue  # Continue to the next iteration of the while loop
    except AttributeError:
        print("Password must be at least 8 characters long")
        continue  # Continue to the next iteration of the while loop