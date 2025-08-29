
"""
Caesar Cipher Program
----------------------
A simple Python implementation of the Caesar Cipher algorithm that allows users to encrypt or decrypt text
using a shift key. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted
a certain number of places down or up the alphabet.

Author: Aryan Jasrotia
"""

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts the given text using Caesar Cipher.
    
    Args:
        text (str): The input message to encrypt or decrypt.
        shift (int): The number of positions to shift.
        mode (str): Either 'encrypt' or 'decrypt'.
    
    Returns:
        str: The resulting encrypted or decrypted message.
    """
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep special characters unchanged

    return result


def get_user_input() -> tuple[str, str, int]:
    """
    Handles user input for mode, text, and shift.
    
    Returns:
        tuple: mode, message, and shift value
    """
    print("=== Caesar Cipher Tool ===")
    print("This tool helps you encrypt or decrypt messages using the Caesar Cipher algorithm.\n")

    while True:
        mode = input("Choose mode [encrypt / decrypt]: ").strip().lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
            print("❌ Invalid choice. Please type 'encrypt' or 'decrypt'.")

    message = input("\nEnter your message: ")

    while True:
        try:
            shift = int(input("Enter shift value (can be negative too): "))
            break
        except ValueError:
            print("❌ Shift must be a number. Try again.")

    return mode, message, shift


def main():
    """
    The main driver function to run the Caesar Cipher program.
    """
    mode, message, shift = get_user_input()
    result = caesar_cipher(message, shift, mode)

    print("\n=== Result ===")
    print(f"Mode: {mode.capitalize()}")
    print(f"Original Message: {message}")
    print(f"Shift Value: {shift}")
    print(f"Processed Message: {result}")
    print("=================\n")


if __name__ == "__main__":
    main()
