from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, add_to_sample, random_number_between


def generate_sample_add():
    def f(sample):
        sample_set = set()
        for j in range(N_TIMES):
            init = get_current_time()
            sample_set.add(j)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_clear():
    def f(sample):
        for j in range(N_TIMES):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.clear()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_copy():
    def f(sample):
        for j in range(N_TIMES):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.copy()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove():
    def f(sample):
        for j in range(1, N_TIMES):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.remove(0)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in():
    def f(sample):
        for j in range(N_TIMES):
            set_sample = [i for i in range(j)]
            index = random_number_between(end=j)
            init = get_current_time()
            index in set_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)
