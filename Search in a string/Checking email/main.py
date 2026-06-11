def check_email(email):
    if " " in email or "@" not in email or "@." in email:
        return False

    at_index = email.index("@")

    if "." not in email[at_index + 1:]:
        return False

    return True