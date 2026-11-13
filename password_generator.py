"""Password Generator — a beginner-friendly Python cybersecurity project.

Generates random, strong passwords with letters, digits, and symbols.
Uses the `secrets` module, which is designed for passwords and tokens.
"""

import argparse
import secrets
import string
import sys

AMBIGUOUS = "l1IoO0"


def generate_password(length: int = 16, use_symbols: bool = True,
                      use_digits: bool = True, use_upper: bool = True,
                      use_lower: bool = True, exclude_ambiguous: bool = False) -> str:
    """Generate a random password with the requested character sets."""
    alphabet = ""
    required = []

    if use_lower:
        chars = string.ascii_lowercase
        alphabet += chars
        required.append(secrets.choice(chars))
    if use_upper:
        chars = string.ascii_uppercase
        alphabet += chars
        required.append(secrets.choice(chars))
    if use_digits:
        chars = string.digits
        alphabet += chars
        required.append(secrets.choice(chars))
    if use_symbols:
        chars = string.punctuation
        alphabet += chars
        required.append(secrets.choice(chars))

    if not alphabet:
        raise ValueError("At least one character set must be enabled.")
    if length < len(required):
        raise ValueError(
            f"Length must be at least {len(required)} to include "
            "one character from each selected set."
        )

    if exclude_ambiguous:
        alphabet = "".join(c for c in alphabet if c not in AMBIGUOUS)
        required = [c for c in required if c not in AMBIGUOUS]
        if not required:
            required = [secrets.choice(alphabet)]

    password = required + [secrets.choice(alphabet) for _ in range(length - len(required))]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate a random, strong password.")
    parser.add_argument("--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("--count", type=int, default=1, help="How many passwords to generate (default: 1)")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--exclude-ambiguous", action="store_true",
                        help="Exclude ambiguous characters like l, 1, I, O, 0")
    args = parser.parse_args(argv)

    if args.length < 4:
        print("Error: length must be at least 4.", file=sys.stderr)
        return 2
    if args.count < 1:
        print("Error: count must be at least 1.", file=sys.stderr)
        return 2

    try:
        for _ in range(args.count):
            print(generate_password(
                length=args.length,
                use_symbols=not args.no_symbols,
                use_digits=not args.no_digits,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                exclude_ambiguous=args.exclude_ambiguous,
            ))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
