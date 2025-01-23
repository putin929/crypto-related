from cipher import CaesarCipher

def main():
    print("Welcome to the Caesar Cipher Tool!")
    shift = int(input("Enter the shift value (key): "))
    cipher = CaesarCipher(shift)

    action = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if action == 'e':
        text = input("Enter the text to encrypt: ")
        result = cipher.encrypt(text)
        print(f"Encrypted text: {result}")
    elif action == 'd':
        text = input("Enter the text to decrypt: ")
        result = cipher.decrypt(text)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid action!")

if __name__ == "__main__":
    main()