"""
Example demonstrations of the Vigenère cipher
"""

from vigenere_cipher import encrypt, decrypt


def main():
    """Run various examples of the Vigenère cipher in action."""
    
    print("🔐 Vigenère Cipher Examples")
    print("=" * 50)
    
    # Example 1: Basic encryption and decryption
    print("\n📝 Example 1: Basic Usage")
    message1 = "welcome to bitcoin"
    key1 = "python"
    encrypted1 = encrypt(message1, key1)
    decrypted1 = decrypt(encrypted1, key1)
    
    print(f"Original:  {message1}")
    print(f"Key:       {key1}")
    print(f"Encrypted: {encrypted1}")
    print(f"Decrypted: {decrypted1}")
    print(f"Match:     {message1 == decrypted1}")
    
    # Example 2: Different key length
    print("\n📝 Example 2: Short Key with Long Message")
    message2 = "this is a longer message to demonstrate key repetition"
    key2 = "key"
    encrypted2 = encrypt(message2, key2)
    decrypted2 = decrypt(encrypted2, key2)
    
    print(f"Original:  {message2}")
    print(f"Key:       {key2}")
    print(f"Encrypted: {encrypted2}")
    print(f"Decrypted: {decrypted2}")
    print(f"Match:     {message2 == decrypted2}")
    
    # Example 3: Message with punctuation and numbers
    print("\n📝 Example 3: Mixed Content (Letters, Numbers, Punctuation)")
    message3 = "hello, world! this is test #123."
    key3 = "secret"
    encrypted3 = encrypt(message3, key3)
    decrypted3 = decrypt(encrypted3, key3)
    
    print(f"Original:  {message3}")
    print(f"Key:       {key3}")
    print(f"Encrypted: {encrypted3}")
    print(f"Decrypted: {decrypted3}")
    print(f"Match:     {message3 == decrypted3}")
    
    # Example 4: Different keys produce different results
    print("\n📝 Example 4: Same Message, Different Keys")
    message4 = "secret message"
    keys = ["python", "java", "cipher", "code"]
    
    print(f"Original message: {message4}")
    print("Encrypted with different keys:")
    for key in keys:
        encrypted = encrypt(message4, key)
        print(f"  Key '{key}': {encrypted}")
    
    # Example 5: Demonstrating case insensitivity
    print("\n📝 Example 5: Case Handling")
    message5_upper = "HELLO WORLD"
    message5_lower = "hello world"
    message5_mixed = "HeLLo WoRLd"
    key5 = "python"
    
    print("All variations produce the same encrypted result:")
    print(f"'{message5_upper}' -> {encrypt(message5_upper, key5)}")
    print(f"'{message5_lower}' -> {encrypt(message5_lower, key5)}")
    print(f"'{message5_mixed}' -> {encrypt(message5_mixed, key5)}")


def interactive_demo():
    """Interactive demo allowing user input."""
    print("\n🎮 Interactive Demo")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            message = input("Enter message to encrypt: ").strip()
            key = input("Enter encryption key: ").strip()
            if message and key:
                encrypted = encrypt(message, key)
                print(f"Encrypted message: {encrypted}")
            else:
                print("Please provide both message and key.")
                
        elif choice == '2':
            message = input("Enter message to decrypt: ").strip()
            key = input("Enter decryption key: ").strip()
            if message and key:
                decrypted = decrypt(message, key)
                print(f"Decrypted message: {decrypted}")
            else:
                print("Please provide both message and key.")
                
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
    
    # Uncomment the line below for interactive demo
    # interactive_demo()
