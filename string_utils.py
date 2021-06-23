
def slice_right(string, index):
    return string[:index]

def slice_left(string, index):
    return string[-index:]

def __get_current_substring_suffix(self, current_substring, post_text_pattern_score):
    return current_substring[-post_text_pattern_score:]


def __get_next_substring_prefix(self, current_substring, prefixScore):
    return current_substring[:prefixScore]


def __get_next_prefix(prefixString, prefixScore):
    return prefixString[-prefixScore:]