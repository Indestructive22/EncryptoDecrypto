def encrypt_char(char, shift, needSub):
    char_code = ord(char)
    if needSub:
        char_code -= 26
    char_code += shift
    
    return chr(char_code)
        

def encrypt_message(message, listo, needSub):
    encrypted_message = ""
    for i, char in enumerate(message):
        tmp = encrypt_char(char, listo[i], needSub[i])
        encrypted_message += tmp
    return encrypted_message
