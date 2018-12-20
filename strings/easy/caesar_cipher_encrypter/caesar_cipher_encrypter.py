def caesar_cipher_encrypter(string, key):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    new_key = key % 26
    transformed_string = ''
    
    for letter in string:
        new_letter = get_new_letter(letter, new_key_alpha)
    return transformed_string

def get_new_letter(letter, key, alpha):
    new_letter_index = alpha.index(letter) + key
    return alpha[new_letter_index] if new_letter_index <= 25 else alpha[-1 + new_letter_index % 25]
