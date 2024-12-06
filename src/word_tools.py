from collections import Counter


def count_anagrams(text, word):
    # If either text or word is empty, return 0
    if not text or not word:
        return 0

    word_len = len(word)
    word_counter = Counter(word)  
    count = 0

    # Iterate over the text and check each substring of length equal to the word
    for i in range(len(text) - word_len + 1):
        substring = text[i : i + word_len]
        if Counter(substring) == word_counter:
            count += 1

    return count
