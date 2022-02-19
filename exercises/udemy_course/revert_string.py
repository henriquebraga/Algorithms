

def revert_string(string, func):
    return ' '.join([
        func(word) for word in string.split(' ')]
    )


def revert_word(word):
    if len(word) == 0:
        return ''
    
    start = 0
    end = len(word) - 1
    
    word_list = list()
    
    word_list[:0] = word # since we can't assign to a str in python, we are converting to a list of chars
    
    while end > start:
        word_list[start], word_list[end] = word_list[end], word_list[start]
        start += 1
        end -= 1
    
    return ''.join(word_list)
    

def revert_word_recursively(word):
    if len(word) == 0:
        return ''
    
    if len(word) == 1:
        return word

    return word[-1] + revert_word_recursively(word[1:-1]) + word[0]



if __name__ == '__main__':
    for function_revert_string in (revert_word, revert_word_recursively):
        assert revert_string('', function_revert_string) == ''
        assert revert_string('a', function_revert_string) == 'a'
        assert revert_string('word', function_revert_string) == 'drow'
        assert revert_string('tests', function_revert_string) == 'stset'
        assert revert_string('hello there', function_revert_string) == 'olleh ereht'