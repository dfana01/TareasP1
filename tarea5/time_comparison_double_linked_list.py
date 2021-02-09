from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, N_STEP, add_to_sample, random_number_between
from double_linked_list import DoubleLinkedList, Node


def generate_sample_add():
    def f(sample):
        sample_list = DoubleLinkedList()
        for j in range(1, N_TIMES, N_STEP):
            init = get_current_time()
            sample_list.add(Node(j))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_clear():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.clear()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_clone():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.clone()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_index_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.index(Node(1))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_index_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.index(Node(int(list_sample.size / 2)))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_index_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.index(Node(j))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_add_index_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            index = 0
            n = random_number_between()
            init = get_current_time()
            list_sample.add_index(index, Node(n))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_add_index_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            index = int(list_sample.size / 2)
            n = random_number_between()
            init = get_current_time()
            list_sample.add_index(index, Node(n))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_add_index_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            index = j
            n = random_number_between()
            init = get_current_time()
            list_sample.add_index(index, Node(n))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_remove_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.remove(1)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_middle():
    def f(sample):
        for j in range(2, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            index = int(list_sample.size / 2)
            init = get_current_time()
            list_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            index = j
            init = get_current_time()
            list_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            el = list_sample.get(1)
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_middle():
    def f(sample):
        for j in range(2, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            el = list_sample.get(int(list_sample.size / 2))
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            el = list_sample.get(j)
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_add_all():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            init = get_current_time()
            list_sample.add_all(*[Node(i) for i in range(j)])
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_get_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.get(1)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_get_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.get(int(list_sample.size / 2))
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_get_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = DoubleLinkedList()
            list_sample.add_all(*[Node(i) for i in range(j)])
            init = get_current_time()
            list_sample.get(j)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)
