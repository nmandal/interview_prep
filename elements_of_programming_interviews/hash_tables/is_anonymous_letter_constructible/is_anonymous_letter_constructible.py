# O(m+n) time where m and n are the number of characters in the letter and magazine respectively
# O(L) space where L is the number of distinct letters appearing in the letter
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_freqs_in_letter = collections.Counter(letter_text)
    
    # Checks if characters in magazine_text can cover characters in char_freq_in_letter
    for c in magazine_text:
        if c in char_freqs_in_letter:
            char_freqs_in_letter[c] -= 1
            if char_freqs_in_letter[c] == 0:
                del char_freqs_in_letter[c]
                if not char_freqs_in_letter:
                    # All characters in letter text have been matched
                    return True
    
    # Empty char_freqs_in_letter means that every letter can be covered
    return not char_freqs_in_letter
