def encrypt_char(char, shift, cee):
    if char.isalpha():
        is_upper = char.isupper()
        char_code = ord(char) + shift
        if char_code > ord('Z') and is_upper==True:
                char_code=char_code-shift-3
                cee+=1
                return chr(char_code), cee
        if char_code > ord('z') and is_upper==False:
            char_code = char_code-shift-3
            cee+=1
            return chr(char_code), cee
        else:
            return chr(char_code), cee
    else:
        return char , cee

def encrypt_message(message, listo,cs):
    encrypted_message = ""
    i=0
    for char in message:
        encrypted_message += encrypt_char(char, listo[i],cs[i])
        i+=1
    return encrypted_message
