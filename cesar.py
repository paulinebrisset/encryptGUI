class Cesar:
    def __init__(self):
        pass

    @staticmethod
    def crypt(message, shift, newbie=False):
        """
        Encrypts a message using the Caesar cipher.

        Args:
            message (str): The message to encrypt.
            shift (int): The number of positions to shift each character.

        Returns:
            str: The encrypted message.
        """
        encrypted_message = ""
        if newbie:
            print("newbie")
            for char in message:
                if char.isalpha():  # Check if the character is an alphabet letter
                    if char.islower():  # Check if the character is lowercase
                        shifted = (ord(char) - ord("a") + shift) % 26 + ord("a")
                    elif char.isupper():  # Check if the character is uppercase
                        shifted = (ord(char) - ord("A") + shift) % 26 + ord("A")
                    encrypted_message += chr(shifted)
                else:
                    encrypted_message += char  # If the character is not an alphabet letter, keep it unchanged
        else:
            print("not newbie")
            for char in message:
                if (
                    32 <= ord(char) <= 126
                ):  # Check if the character is in the ASCII range 32 to 126
                    shifted = (
                        ord(char) - 32 + shift
                    ) % 95 + 32  # Apply the shift only within this range
                    encrypted_message += chr(shifted)
                else:
                    encrypted_message += char  # If the character is not in the ASCII range, keep it unchanged
        return encrypted_message

    @staticmethod
    def decrypt(message, shift, newbie=False):
        """
        Decrypts a message encrypted using the Caesar cipher.

        Args:
            message (str): The encrypted message.
            shift (int): The number of positions the characters were shifted during encryption.

        Returns:
            str: The decrypted message.
        """
        return Cesar.crypt(message, -shift, newbie)


# Example usage
if __name__ == "__main__":
    cipher = Cesar()
    message = "abcdefghijklmnopqrstuvwxyzéèà"
    shift = 3
    encrypted = cipher.crypt(message, shift)
    decrypted = cipher.decrypt(encrypted, shift)
    print("Original Message:", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
