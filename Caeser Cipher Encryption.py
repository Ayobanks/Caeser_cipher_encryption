message = input("Please enter the text you want to encrypt: ")
shiftkey = int(input("Please enter the key: "))
action = input("Encrypt or Decrypt: ").lower()

if action == "decrypt":
 shiftkey = -shiftkey

ALPHA_BET = 26
RANGE_MAX = ord("Z")
RANGE_MIN = ord("A")


def caesar_shift(message,shiftkey):
    result = ""
    for letter in message:
         if letter.isalpha():
         #Covert sentence to ascii code
             if letter.isupper():
                 base = ord("A")
             else:
                 base = ord("a")

             new_ascii_code = (ord(letter) - base + shiftkey) % 26
             new_letter = chr(new_ascii_code + base)
             result += new_letter

         else:
             result += letter

    print(result)

caesar_shift(message,shiftkey)

    
  