# O(m+n) time where m and n are the number of characters in the letter and magazine respectively
# O(L) space where L is the number of distinct letters appearing in the letter
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))
