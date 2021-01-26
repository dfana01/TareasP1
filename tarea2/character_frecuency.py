from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, add_to_sample, get_random_str


def repeated_character(str):
    chars_dic = {}
    for val in str:
        if val not in chars_dic:
            chars_dic[val] = 1
        else:
            chars_dic[val] += 1
    return chars_dic


def generate_repeated_character():
    def f(sample):
        for j in range(N_TIMES):
            s = get_random_str(j)
            init = get_current_time()
            repeated_character(s)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)
