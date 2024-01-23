def decrypt_char(char, shift, isUp, addedExtra):
    return doTransformation(char, shift, isUp, addedExtra) if char.isalpha() else char
    
def doTransformation(char, shift, isUp, addedExtra):
    char_code = ord(char) - shift if not addedExtra else ord(char) - shift - 7
    return chr(char_code).lower() if not isUp else chr(char_code)


def decrypt_message(encrypted_message, instance):
    decrypted_message = ""
    for i,char in enumerate(encrypted_message):
        decrypted_message += str(decrypt_char(char, instance.listo[i], instance.isUp[i], instance.addedExtra[i]))
    return decrypted_message
