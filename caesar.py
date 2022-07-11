# Nicholas Soluri
# CSC 111 Lab 8 Part 2
# Dr. Burhans
# caesar.py
def encode(sent):
    x = int(input('What key would you like to encode by?: '))
    ciphertext = ''
    for ch in sent:
        if ch not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ciphertext = ciphertext + ch
        if ch >= 'A' and ch <= 'Z':
            ch = (((ord(ch)-65) + x) % 26)
            newch = chr(ch + 65)
            ciphertext = ciphertext + newch
        elif ch >= 'a' and ch <= 'z':
            ch = (((ord(ch)-97) + x) % 26)
            newch = chr(ch + 97)
            ciphertext = ciphertext + newch

    return ciphertext

def decode(sent):
    x = int(input('what key would you like to decode by?: '))
    ciphertext = ''
    for ch in sent:
        if ch not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ciphertext = ciphertext + ch
        if ch >= 'A' and ch <= 'Z':
            ch = (((ord(ch)-65) - x) % 26)
            newch = chr(ch + 65)
            ciphertext = ciphertext + newch
        elif ch >= 'a' and ch <= 'z':
            ch = (((ord(ch)-97) - x) % 26)
            newch = chr(ch + 97)
            ciphertext = ciphertext + newch
            
    return ciphertext














            
    


message = input('Give me a message that you would like to encode/decode: ')
key = input('would you like to encode or decode? type ''en'' or ''de'': ')
if key == 'en':
    print(encode(message))
if key == 'de':
    print(decode(message))
