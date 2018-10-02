import random

list_of_random_strings = ['def', 'class', 'while', 'for']
valid_user_input = list('abcdefghijklmnopqrstuvwxyz')


def get_random_string():
    return random.choice(list_of_random_strings)


def get_user_input():
    user_input = None

    while user_input not in valid_user_input:
        print('> Guess a letter:')
        user_input = input("< ").lower()
        if user_input in valid_user_input:
            return user_input
        else:
            print('Enter a letter!')


def game_process(word):

    # число ошибок которое пользователь может допустить
    num_of_mistakes = len(word)
    # зашифрованное слово
    word_secret = '*' * len(word)

    while True:
        user_letter = yield

        if user_letter in word:
            round_status = True
            word_secret_list = list(word_secret)
            word_secret_list[word.find(user_letter)] = user_letter
            word_secret = ''.join(word_secret_list)
        else:
            round_status = False
            num_of_mistakes -= 1

        if num_of_mistakes == 0:
            return False, num_of_mistakes, len(word), word_secret
        elif '*' not in word_secret:
            return True, num_of_mistakes, len(word), word_secret
        else:
            yield (round_status, num_of_mistakes, len(word), word_secret)


if __name__ == '__main__':
    try:
        g = game_process(get_random_string())

        while True:
            next(g)
            round_result = g.send(get_user_input())
            if round_result[0]:
                print('''> Hit!\n>\n> The word: {0}\n>'''.format(round_result[3]))
            else:
                print(
                    '''> Missed, mistake {0} out of {1}.\n>\n> The word: {2}\n>'''.format(
                        round_result[2] - round_result[1],
                        round_result[2], round_result[3]))

    except StopIteration as e:
        game_result = e.value
        if game_result[0]:
            print('''> Hit!\n>\n> The word: {0}\n>\n>You won!'''.format(game_result[3]))
        else:
            print(
                '''> Missed, mistake {0} out of {1}.\n>\n> The word: {2}\n>\n>You lost!'''.format(
                    game_result[2] - game_result[1],
                    game_result[2], game_result[3]))
