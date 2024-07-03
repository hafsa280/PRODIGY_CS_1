def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char

    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting program.")
            break

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted Text: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted Text: {decrypted_text}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
