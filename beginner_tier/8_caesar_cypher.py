def encrypt_char(char, shift):
    num = (ord(char)+shift-97)%26 +97
    return chr(num)
def encrypt(message, shift):
    """A Caesar Cypher encryption method"""
    cypher= [encrypt_char(char, shift) if char.isalpha() else char for char in message]
    return "".join(cypher)

def decrypt(message, shift):
    """A Caesar Cypher decryption method"""
    
    
method=input("Type encode to encrypt, decode to decrypt\n").lower()


text=input("Type your message\n").lower()
shift = int(input("Type the shift number: \n"))
print(encrypt(text, shift))