import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password(password):
    # Length check
    if not (6 <= len(password) <= 12):
        return False
    
    # Digit check
    if sum(c.isdigit() for c in password) < 1:
        return False
    
    # Lowercase characters check
    if sum(c.islower() for c in password) < 2:
        return False
    
    # Uppercase character check
    if sum(c.isupper() for c in password) < 1:
        return False
    
    # Punctuation character check
    if sum(c in PUNCTUATION_CHARS for c in password) < 1:
        return False
    
    # Previously used check
    if password in used_passwords:
        return False
    
    # If all checks pass, add the password to the used passwords and return True
    used_passwords.add(password)
    return True