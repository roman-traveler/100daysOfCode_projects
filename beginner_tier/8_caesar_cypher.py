def move_char(char, shift):
    """
    Move lower aplhanum char shift positions in table
    Args: char lowercase ASCII
    shift: int position shift,can be negative.
    """
    num = (ord(char) + shift - 97) % 26 + 97
    return chr(num)


def encrypt(message, shift):
    """A Caesar Cypher encryption method"""
    cypher = [move_char(char, shift) if char.isalpha() else char for char in message]
    return "".join(cypher)


def decrypt(message, shift):
    """A Caesar Cypher decryption method"""
    cypher = [move_char(char, -shift) if char.isalpha() else char for char in message]
    return "".join(cypher)


method = input("Type encode to encrypt, decode to decrypt\n").lower()


text = input("Type your message\n").lower()
shift = int(input("Type the shift number: \n"))
match method:
    case "encode":
        print(f"Here is the encrypted message: {encrypt(text, shift)}")
    case "decode":
        print(f"Here is the decrypted message: {decrypt(text, shift)}")
    case _:
        print("Invalid method")
