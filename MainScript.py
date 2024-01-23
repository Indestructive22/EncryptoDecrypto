from encrypt_module import encrypt_char, encrypt_message
from decrypt_module import decrypt_char, decrypt_message
import random

class WordEncoder:
    def __init__(self, word, listo, isUp, addedExtra):
        self.word = word
        self.listo = listo
        self.isUp = isUp
        self.addedExtra = addedExtra
        self.encoded_word, self.updatedAddedExtra = encrypt_message(word, listo, isUp, addedExtra)

def main():
    word_instances = []

    while True:
        print("\nMenu:")
        print("1. Encode a word")
        print("2. Decode a word")
        print("3. Print all words and their encoded versions")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            word = input("Enter the word to encode: ")
            listo = []
            isUp = []
            for char in word:
                if char != " ":
                    listo.append(random.randint(1, 26))
                    isUp.append(char.isupper())
                else:
                    listo.append(0)
                    isUp.append(False)
                    
                # print(listo)
            new_word_instance = WordEncoder(word, listo, isUp, [False]*(len(word)))
            word_instances.append(new_word_instance)
            print(f"Encoded message: {new_word_instance.encoded_word}")

        elif choice == '2':
            if not word_instances:
                print("No words have been encoded yet.")
            else:
                word_to_decode = input("Enter the word to decode: ")
                for instance in word_instances:
                    if instance.encoded_word == word_to_decode:
                        decoded_word = decrypt_message(word_to_decode, instance)
                        print(f"Decoded message: {decoded_word}")
                        # Remove the break statement here
                        # break

        elif choice == '3':
            if not word_instances:
                print("No words have been encoded yet.")
            else:
                for instance in word_instances:
                    print(f"Original: {instance.word}, Encoded: {instance.encoded_word}")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
