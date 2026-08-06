#!/usr/bin/env python3
"""Generate random secure passwords.

Usage:
    python password_generator.py [length] [--no-symbols]
"""

import secrets
import string
import sys


def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    """
    Generate a cryptographically secure random password.

    Args:
        length: Desired password length (default 16).
        use_symbols: Include special characters if True.

    Returns:
        A random password string.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8")

    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%^&*"

    return ''.join(secrets.choice(chars) for _ in range(length))


def main():
    length = 16
    use_symbols = True

    args = sys.argv[1:]
    for arg in args:
        if arg == "--no-symbols":
            use_symbols = False
        elif arg.isdigit():
            length = int(arg)

    try:
        pwd = generate_password(length, use_symbols)
        print(pwd)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()