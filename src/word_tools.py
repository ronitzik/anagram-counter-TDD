from collections import Counter


def count_anagrams(text, word):
    if not text or not word or len(word) > len(text):
        return 0

    word_len = len(word)
    word_counter = Counter(word)
    current_counter = Counter(text[:word_len])  # Initialize with the first window
    count = 0

    # If the first window matches the word, increment the count
    if current_counter == word_counter:
        count += 1

    # Sliding window approach
    for i in range(word_len, len(text)):
        # Add the new character
        current_counter[text[i]] += 1

        # Remove the old character
        current_counter[text[i - word_len]] -= 1
        if current_counter[text[i - word_len]] == 0:
            del current_counter[text[i - word_len]]  

        # Compare the current window with the word's counter
        if current_counter == word_counter:
            count += 1

    return count
