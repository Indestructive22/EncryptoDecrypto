def decrypt_char(char, shift, needSub):
    return doTransformation(char, shift, needSub)
    
def doTransformation(char, shift, needSub):
    n = ord(char) - shift if not needSub else ord(char) - shift + 26
    return chr(n)


def decrypt_message(encrypted_message, instance):
    decrypted_message = ""
    for i,char in enumerate(encrypted_message):
        decrypted_message += str(decrypt_char(char, instance.listo[i], instance.needSub[i]))
    return decrypted_message
