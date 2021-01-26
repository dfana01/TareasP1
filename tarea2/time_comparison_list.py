from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, add_to_sample, \
    graph_men_and_time


def generate_sample_append():
    def f(sample):
        sample_list = []
        for j in range(N_TIMES):
            init = get_current_time()
            sample_list.append(j)
            delta = get_current_time() - init
            men = get_current_ram()
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_clear():
    pass


def generate_sample_copy():
    pass


def generate_sample_index():
    pass


def generate_sample_insert():
    pass


def generate_sample_remove():
    pass


def generate_sample_sort():
    pass


def generate_sample_in():
    pass


if __name__ == '__main__':
    graph_men_and_time(generate_sample_append(), "List Append")
