def encrypt_char(char, shift, isUp, addedExtra):
    if char.isalpha():
        if not isUp:
             char = char.upper()
        char_code = ord(char) + shift
        if char_code > ord('Z') and char_code < ord('a'):
                char_code = char_code + 7
                addedExtra = True
        
        return chr(char_code), addedExtra
        
    else:
        return char, False

def encrypt_message(message, listo, isUp, addedExtra):
    encrypted_message = ""
    for i, char in enumerate(message):
        tmp = encrypt_char(char, listo[i], isUp[i], addedExtra[i])
        addedExtra[i] = tmp[1]
        encrypted_message += tmp[0]
    return encrypted_message, addedExtra
