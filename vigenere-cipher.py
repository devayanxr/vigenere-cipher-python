"""
Vigenère Cipher Implementation
Part of freeCodeCamp's Scientific Computing with Python curriculum

Copyright (c) 2025 Devayan Das
Licensed under the MIT License

This module provides functions to encrypt and decrypt messages using the Vigenère cipher,
a polyalphabetic substitution cipher that uses a keyword to determine character shifts.

Author: Devayan Das
GitHub: https://github.com/devayanxr
Email: devayandas884@gmail.com
"""

def vigenere(message, key, direction=1):
    """
    Core Vigenère cipher function that can encrypt or decrypt based on direction.
    
    Args:
        message (str): The text to be processed
        key (str): The keyword used for encryption/decryption
        direction (int): 1 for encryption, -1 for decryption
    
    Returns:
        str: The processed message
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the message unchanged
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message


def encrypt(message, key):
    """
    Encrypt a message using the Vigenère cipher.
    
    Args:
        message (str): The plaintext message to encrypt
        key (str): The keyword to use for encryption
    
    Returns:
        str: The encrypted message
    
    Example:
        >>> encrypt("hello world", "python")
        'wrald jyvnd'
    """
    return vigenere(message, key)


def decrypt(message, key):
    """
    Decrypt a message using the Vigenère cipher.
    
    Args:
        message (str): The encrypted message to decrypt
        key (str): The keyword used for decryption (same as encryption key)
    
    Returns:
        str: The decrypted message
    
    Example:
        >>> decrypt("wrald jyvnd", "python")
        'hello world'
    """
    return vigenere(message, key, -1)


if __name__ == "__main__":
    # Example usage and demonstration
    text = 'mrttaqrhknsw ih puggrur'
    custom_key = 'python'
    
    print("=== Vigenère Cipher Demo ===")
    print(f"Encrypted text: {text}")
    print(f"Key: {custom_key}")
    
    decryption = decrypt(text, custom_key)
    print(f"Decrypted text: {decryption}")
    
    # Verify the process works both ways
    print("\n=== Verification Test ===")
    test_message = "hello world"
    encrypted = encrypt(test_message, custom_key)
    decrypted_back = decrypt(encrypted, custom_key)
    
    print(f"Original: {test_message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted_back}")
    print(f"Process successful: {test_message == decrypted_back}")
