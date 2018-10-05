from hangman.hangman import get_random_string, game_process


def test_get_random_string():
    for i in range(100):
        assert True == (get_random_string() in ['def', 'class', 'while', 'for'])