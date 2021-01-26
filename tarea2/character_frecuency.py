

def repeated_character(str):
    chars_dic = {}
    for val in str:
        if val not in chars_dic:
            chars_dic[val] = 1
        else:
            chars_dic[val] += 1
    return chars_dic


if __name__ == '__main__':
    print(repeated_character(input()))

