from operator import xor
contents = open('encryptedtext.txt').read().split(',')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def decrypt(text, key):
    newtext = ''
    for n in range(len(text)):
        newtext += chr(xor(int(text[n]), key[n%3]))
    return newtext

def PE059():
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                key = [ord(i), ord(j), ord(k)]
                string = decrypt(contents, key)
                if 'the' in string and '^' not in string and '$' not in string and '@' not in string and '%' not in string and '#' not in string:
                    return sum([ord(i) for i in string])
print(PE059())