def decrypt_char(char, shift, cee):
    if char.isalpha():
        is_upper = char.isupper()
        print (shift)
        char_code=ord(char)
        if char_code+shift>ord('z') and cee==1:
            char_code += (2*shift)+3
            return chr(char_code)
        else:
            char_code = ord(char) - shift
            return chr(char_code)
    else:
            print(shift)
            if cee!=0:
                return ord(char)
            else:
                return char

def decrypt_message(encrypted_message, listo, cs):
    decrypted_message = ""
    i=0
    for char in encrypted_message:
        decrypted_message += str(decrypt_char(char, listo[i], cs[i]))
        i+=1
    return decrypted_message
