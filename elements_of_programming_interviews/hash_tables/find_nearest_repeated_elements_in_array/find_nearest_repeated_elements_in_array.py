# O(n) time | O(d) space where d is the number of distinct elements in array
def find_nearest_repeated_elements_in_array(array):
    word_to_latest_idx, nearest_repeated = {}, float('inf')
    for i, ele in enumerate(array):
        if word in word_to_latest_idx:
            curr = word_to_latest_idx[word]
            nearest_repeated = min(i - curr, nearest_repeated)
        word_to_latest_idx[word] = i
    return nearest_repeated
