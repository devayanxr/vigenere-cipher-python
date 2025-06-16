"""
Test suite for the Vigenère cipher implementation
Tests various edge cases and functionality
"""

from vigenere_cipher import encrypt, decrypt


def test_basic_functionality():
    """Test basic encryption and decryption."""
    print("Testing basic functionality...")
    
    # Test case 1: Simple message
    message = "hello"
    key = "key"
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    
    assert decrypted == message, f"Failed: {message} != {decrypted}"
    print("✓ Basic encryption/decryption works")
    
    # Test case 2: The given example
    encrypted_text = 'mrttaqrhknsw ih puggrur'
    custom_key = 'python'
    expected_result = 'welcome to bitcoin'
    
    result = decrypt(encrypted_text, custom_key)
    assert result == expected_result, f"Failed: Expected '{expected_result}', got '{result}'"
    print("✓ Given example decrypts correctly")


def test_edge_cases():
    """Test various edge cases."""
    print("\nTesting edge cases...")
    
    # Test case 1: Empty message
    result = encrypt("", "key")
    assert result == "", "Failed: Empty message should return empty string"
    print("✓ Empty message handled correctly")
    
    # Test case 2: Single character
    result = encrypt("a", "b")
    expected = "b"  # 'a' + 1 = 'b'
    assert result == expected, f"Failed: Expected '{expected}', got '{result}'"
    print("✓ Single character encryption works")
    
    # Test case 3: Key longer than message
    message = "hi"
    key = "verylongkey"
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    assert decrypted == message, "Failed: Long key with short message"
    print("✓ Long key with short message works")


def test_non_alphabetic_characters():
    """Test handling of non-alphabetic characters."""
    print("\nTesting non-alphabetic characters...")
    
    # Test case 1: Numbers and punctuation
    message = "hello, world! 123"
    key = "test"
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    
    assert decrypted == message, f"Failed: {message} != {decrypted}"
    print("✓ Numbers and punctuation preserved")
    
    # Test case 2: Only non-alphabetic characters
    message = "123 !@# $%^"
    key = "test"
    encrypted = encrypt(message, key)
    
    assert encrypted == message, "Failed: Non-alphabetic only message should remain unchanged"
    print("✓ Non-alphabetic only messages unchanged")


def test_case_insensitivity():
    """Test case handling."""
    print("\nTesting case handling...")
    
    messages = ["HELLO", "hello", "HeLLo", "hELLO"]
    key = "test"
    
    # All should produce the same encrypted result
    encrypted_results = [encrypt(msg, key) for msg in messages]
    
    # Check all results are the same
    first_result = encrypted_results[0]
    for result in encrypted_results[1:]:
        assert result == first_result, f"Failed: Case variations produce different results"
    
    print("✓ Case insensitivity works correctly")


def test_key_repetition():
    """Test that key repetition works correctly."""
    print("\nTesting key repetition...")
    
    # Short key with long message
    message = "abcdefghijklmnop"
    key = "abc"
    
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    
    assert decrypted == message, "Failed: Key repetition not working"
    print("✓ Key repetition works correctly")


def test_reversibility():
    """Test that encryption and decryption are reversible."""
    print("\nTesting reversibility...")
    
    test_cases = [
        ("hello world", "python"),
        ("the quick brown fox", "key"),
        ("testing 123 !@#", "secret"),
        ("", "key"),
        ("a", "z"),
        ("python programming is fun", "vigenere")
    ]
    
    for message, key in test_cases:
        encrypted = encrypt(message, key)
        decrypted = decrypt(encrypted, key)
        assert decrypted == message, f"Failed reversibility test: '{message}' with key '{key}'"
    
    print("✓ All reversibility tests passed")


def test_known_vectors():
    """Test against known encryption vectors."""
    print("\nTesting known vectors...")
    
    # Known test vectors for Vigenère cipher
    test_vectors = [
        ("attackatdawn", "lemon", "lxfopvefrnhr"),
        ("hello", "world", "dqllq"),
        ("cryptography", "key", "mzuxcvkxpbc")
    ]
    
    for plaintext, key, expected_ciphertext in test_vectors:
        result = encrypt(plaintext, key)
        assert result == expected_ciphertext, f"Failed known vector: {plaintext} + {key} should be {expected_ciphertext}, got {result}"
    
    print("✓ Known vector tests passed")


def run_all_tests():
    """Run all tests."""
    print("🧪 Running Vigenère Cipher Tests")
    print("=" * 50)
    
    try:
        test_basic_functionality()
        test_edge_cases()
        test_non_alphabetic_characters()
        test_case_insensitivity()
        test_key_repetition()
        test_reversibility()
        test_known_vectors()
        
        print("\n✅ All tests passed!")
        print("The Vigenère cipher implementation is working correctly.")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False
    
    return True


if __name__ == "__main__":
    run_all_tests()
