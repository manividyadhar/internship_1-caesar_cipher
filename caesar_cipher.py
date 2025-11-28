"""
Caesar Cipher Encryption/Decryption Tool
Description: A Python implementation of the Caesar Cipher algorithm for encrypting and decrypting text messages.
"""

def encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher algorithm.
    
    Args:
        text (str): The message to encrypt
        shift (int): Number of positions to shift (0-25)
    
    Returns:
        str: Encrypted message
    
    Example:
        >>> encrypt("Hello", 3)
        'Khoor'
    """
    result = ""
    
    for char in text:
        if char.isupper():
            # Encrypt uppercase letters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Encrypt lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def decrypt(text, shift):
    """
    Decrypts text using Caesar Cipher algorithm.
    
    Args:
        text (str): The message to decrypt
        shift (int): Number of positions to shift back (0-25)
    
    Returns:
        str: Decrypted message
    
    Example:
        >>> decrypt("Khoor", 3)
        'Hello'
    """
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)


def brute_force_decrypt(text):
    """
    Attempts to decrypt a message by trying all possible shifts (0-25).
    Useful when the shift value is unknown.
    
    Args:
        text (str): The encrypted message
    
    Returns:
        None: Prints all possible decryptions
    """
    print("\n" + "=" * 60)
    print("BRUTE FORCE DECRYPTION - All Possible Shifts")
    print("=" * 60)
    
    for shift in range(26):
        decrypted = decrypt(text, shift)
        print(f"Shift {shift:2d}: {decrypted}")


def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 60)
    print("         CAESAR CIPHER ENCRYPTION/DECRYPTION TOOL")
    print("=" * 60)
    print("\nChoose an option:")
    print("  1. Encrypt a message")
    print("  2. Decrypt a message")
    print("  3. Brute Force Decrypt (try all shifts)")
    print("  4. Exit")
    print("-" * 60)


def get_valid_shift():
    """
    Gets a valid shift value from the user.
    
    Returns:
        int: Valid shift value between 0-25
    """
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("⚠ Shift must be between 0 and 25. Try again.")
        except ValueError:
            print("⚠ Invalid input! Please enter a number.")


def main():
    """Main function to run the Caesar Cipher program."""
    
    print("Welcome to Caesar Cipher Tool!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        
        if choice == '4':
            print("\n" + "=" * 60)
            print("Thank you for using Caesar Cipher Tool! 🔒")
            print("=" * 60 + "\n")
            break
        
        if choice not in ['1', '2', '3']:
            print("\n Invalid choice! Please enter 1, 2, 3, or 4.")
            continue
        
        # Get message from user
        message = input("\nEnter your message: ")
        
        if not message:
            print(" Message cannot be empty!")
            continue
        
        # Handle brute force option
        if choice == '3':
            brute_force_decrypt(message)
            input("\nPress Enter to continue...")
            continue
        
        # Get shift value for encrypt/decrypt
        shift = get_valid_shift()
        
        # Perform encryption or decryption
        if choice == '1':
            encrypted = encrypt(message, shift)
            print("\n" + "=" * 60)
            print("ENCRYPTION RESULT")
            print("=" * 60)
            print(f"Original Message:  {message}")
            print(f"Shift Value:       {shift}")
            print(f"Encrypted Message: {encrypted}")
            print("=" * 60)
        else:  # choice == '2'
            decrypted = decrypt(message, shift)
            print("\n" + "=" * 60)
            print("DECRYPTION RESULT")
            print("=" * 60)
            print(f"Encrypted Message: {message}")
            print(f"Shift Value:       {shift}")
            print(f"Decrypted Message: {decrypted}")
            print("=" * 60)
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()