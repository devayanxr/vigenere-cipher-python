# Learn String Manipulation by Building a Cipher

## Project Overview

Python is a powerful and popular programming language widely used for data science, data visualization, web development, game development, machine learning and more.

In this project, you'll learn fundamental programming concepts in Python, such as variables, functions, loops, and conditional statements. You'll use these to code your first programs.

## About This Project

This project implements a **Vigenère Cipher** - a classical polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages. The Vigenère cipher is more secure than simple substitution ciphers because it uses multiple Caesar ciphers based on the letters of a keyword.

### What You'll Learn

- String manipulation and character operations
- Modular arithmetic for cipher operations
- Function design and implementation
- Loop structures and conditional statements
- Working with alphabetic characters and indices

## How the Vigenère Cipher Works

The Vigenère cipher uses a keyword to determine how much to shift each letter in the message:

1. **Keyword Repetition**: The keyword is repeated to match the length of the message
2. **Character Shifting**: Each letter in the message is shifted by the corresponding letter value in the keyword
3. **Modular Arithmetic**: Uses modulo 26 to wrap around the alphabet

### Example
- **Message**: "hello world"
- **Key**: "python"
- **Encrypted**: "wrald jyvnd"

## Features

- **Encryption**: Convert plain text to cipher text using a keyword
- **Decryption**: Convert cipher text back to plain text using the same keyword
- **Case Handling**: Automatically converts to lowercase for processing
- **Non-alphabetic Characters**: Preserves spaces and punctuation
- **Flexible Key Length**: Works with keywords of any length

## Files Structure

```
vigenere-cipher/
│
├── README.md              # This file
├── vigenere_cipher.py     # Main cipher implementation
├── examples.py            # Usage examples and demonstrations
└── tests.py              # Test cases to verify functionality
```

## Usage

### Basic Usage

```python
from vigenere_cipher import encrypt, decrypt

# Encrypt a message
message = "welcome to bitcoin"
key = "python"
encrypted = encrypt(message, key)
print(f"Encrypted: {encrypted}")  # Output: mrttaqrhknsw ih puggrur

# Decrypt the message
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")  # Output: welcome to bitcoin
```

### Running the Examples

```bash
python examples.py
```

### Running Tests

```bash
python tests.py
```

## Algorithm Details

The cipher uses the following formula:
- **Encryption**: `(message_char_index + key_char_index) % 26`
- **Decryption**: `(message_char_index - key_char_index) % 26`

Where character indices are based on their position in the alphabet (a=0, b=1, ..., z=25).

## Part of freeCodeCamp Curriculum

This project is part of the **Scientific Computing with Python** certification from freeCodeCamp. It demonstrates fundamental programming concepts through practical cryptography implementation.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this project and submit pull requests for improvements or additional features.

---

*This project was created as part of the freeCodeCamp Scientific Computing with Python curriculum.*
