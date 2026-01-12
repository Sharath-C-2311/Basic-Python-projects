import string

UPPER = string.ascii_uppercase   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
LOWER = string.ascii_lowercase   # abcdefghijklmnopqrstuvwxyz

# Example monoalphabetic key (must be 26 unique letters)
KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Build mapping tables
enc_upper = dict(zip(UPPER, KEY))
dec_upper = dict(zip(KEY, UPPER))

enc_lower = dict(zip(LOWER, KEY.lower()))
dec_lower = dict(zip(KEY.lower(), LOWER))


def encrypt(text):
    result = ""

    for ch in text:
        if ch in enc_upper:
            result += enc_upper[ch]
        elif ch in enc_lower:
            result += enc_lower[ch]
        else:
            result += ch   # numbers, spaces, symbols unchanged

    return result


def decrypt(text):
    result = ""

    for ch in text:
        if ch in dec_upper:
            result += dec_upper[ch]
        elif ch in dec_lower:
            result += dec_lower[ch]
        else:
            result += ch

    return result


# -------- Example --------
print("\n--------Monoalphabetic Substitution Cipher---------")
print("---------------------------------------------------")
print("Key obeyed between sender and receiver:")
print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
print(" ".join(KEY))
print("---------------------------------------------------")
print("Sender :")
msg = input("Enter message: ")
cipher = encrypt(msg)
plain = decrypt(cipher)

print("Plaintext :", msg)
print("Encrypted :", cipher)

print("\nReceiver :")
print("Encrypted :", cipher)
print("Decrypted :", plain)
print("\n---------------------------------------------------")