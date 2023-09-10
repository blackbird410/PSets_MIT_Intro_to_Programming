from hangman import *


def test_is_word_guessed():
    assert is_word_guessed("apple", ['e', 'i', 'k', 'p', 'r', 's']) == False


def test_get_gessed_word():
    assert get_guessed_word("apple", ['e', 'i', 'k', 'p', 'r', 's']) == "_ pp_ e"


def test_get_available_letters():
    assert get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) == "abcdfghjlmnoqtuvwxyz"


def test_match_with_gaps():
    assert match_with_gaps("te_ t", "tact") ==  False
    assert match_with_gaps("a_ _ le", "banana") ==  False
    assert match_with_gaps("a_ _ le", "apple") == True
    assert match_with_gaps("a_ ple", "apple") == False


def test_show_possible_matches():
    assert show_possible_matches("t_ _ t") == "tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit"
