from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, add_to_sample, random_number_between


def generate_sample_append():
    def f(sample):
        sample_list = []
        for j in range(N_TIMES):
            init = get_current_time()
            sample_list.append(j)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_clear():
    def f(sample):
        for j in range(N_TIMES):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.clear()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_copy():
    def f(sample):
        for j in range(N_TIMES):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.copy()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_index():
    def f(sample):
        for j in range(1, N_TIMES):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.index(0)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_insert():
    def f(sample):
        for j in range(N_TIMES):
            list_sample = [i for i in range(j)]
            index = random_number_between(end=j)
            init = get_current_time()
            list_sample.insert(index, index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_remove():
    def f(sample):
        for j in range(1, N_TIMES):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.remove(0)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_sort():
    def f(sample):
        for j in range(N_TIMES):
            list_sample = [random_number_between() for i in range(j)]
            init = get_current_time()
            list_sample.sort()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in():
    def f(sample):
        for j in range(N_TIMES):
            list_sample = [i for i in range(j)]
            index = random_number_between(end=j)
            init = get_current_time()
            index in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)
