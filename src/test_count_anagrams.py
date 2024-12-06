import pytest
from word_tools import count_anagrams
import time


def test_empty_text():
    assert count_anagrams("", "abc") == 0


def test_empty_word():
    assert count_anagrams("abcdef", "") == 0


def test_word_longer_than_text():
    assert count_anagrams("ab", "abcdef") == 0


def test_single_anagram_in_text():
    assert count_anagrams("forxxorfxdofr", "for") == 3


def test_multiple_anagrams_in_text():
    assert count_anagrams("abcdabcd", "abc") == 2


def test_no_anagrams_in_text():
    assert count_anagrams("xyzxyz", "abc") == 0


def test_single_letter_word():
    assert count_anagrams("aabbcc", "a") == 2


def test_text_equals_word():
    assert count_anagrams("abc", "abc") == 1


def test_identical_anagrams():
    assert count_anagrams("aaa", "aa") == 2


def test_anagrams_at_the_end():
    assert count_anagrams("abcdabcd", "dcb") == 2


def test_count_anagrams_performance():
    text = "forxxorfxdofr" * 100 
    word = "for"
    
    start_time = time.time()
   
    for _ in range(1000):
        count_anagrams(text, word)
    
    # Calculate the elapsed time in milliseconds
    elapsed_time = (time.time() - start_time) * 1000  
    
    print(f"Time taken to run count_anagrams 1000 times: {elapsed_time:.2f} ms")
    
    assert elapsed_time <  3048.47, f"Performance test failed. Took {elapsed_time:.2f} ms."
