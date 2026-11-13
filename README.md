# Password Generator 🔐

A beginner-friendly Python cybersecurity project that generates
random, strong passwords with letters, digits, and symbols.

## Features

- Generates passwords of any length
- Includes uppercase, lowercase, digits, and symbols by default
- Guarantees at least one character from each selected set
- Uses `secrets`, Python's module for passwords and tokens
- Can generate several passwords at once
- Can exclude ambiguous characters like `l`, `1`, `I`, `O`, `0`

## Requirements

- Python 3.8 or newer
- No third-party packages are required

## How to run

```bash
python password_generator.py
```

On some systems, use `python3 password_generator.py`.

### Examples

Generate one 16-character password (the default):

```bash
python password_generator.py
```

Generate a 24-character password:

```bash
python password_generator.py --length 24
```

Generate 5 passwords at once:

```bash
python password_generator.py --count 5
```

Generate a password without symbols:

```bash
python password_generator.py --no-symbols
```

Generate a password without ambiguous characters:

```bash
python password_generator.py --exclude-ambiguous
```

## Project structure

```text
password-generator/
├── password_generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Learning outcomes

- Random generation with `secrets` (not `random`, for passwords)
- Command-line arguments with `argparse`
- String handling and character sets
- Basic password-security concepts

## Author

SHANMUKHA SREE LALITHA VENKAT SHYAM PYNA ([@1shyam253](https://github.com/1shyam253))
