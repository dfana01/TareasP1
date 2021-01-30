from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, N_STEP, add_to_sample


def generate_sample_add():
    def f(sample):
        sample_set = set()
        for j in range(0, N_TIMES, N_STEP):
            init = get_current_time()
            sample_set.add(j)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_clear():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.clear()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_copy():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.copy()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            index = min(set_sample)
            init = get_current_time()
            set_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            index = int(j / 2)
            init = get_current_time()
            set_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            index = max(set_sample)
            init = get_current_time()
            set_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = set([i for i in range(j)])
            el = 0
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = set([i for i in range(j)])
            el = int(j / 2)
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = set([i for i in range(j)])
            el = j-1
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


