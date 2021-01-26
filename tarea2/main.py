from character_frecuency import generate_repeated_character
import time_comparison_list
import time_comparison_set
from util import graph_men_and_time


def main():
    # List
    list_samples = [
        {"func": time_comparison_list.generate_sample_append, "title": "List Append"},
        {"func": time_comparison_list.generate_sample_clear, "title": "List clear"},
        {"func": time_comparison_list.generate_sample_copy, "title": "List copy"},
        {"func": time_comparison_list.generate_sample_index, "title": "List index"},
        {"func": time_comparison_list.generate_sample_insert, "title": "List insert"},
        {"func": time_comparison_list.generate_sample_remove, "title": "List remove"},
        {"func": time_comparison_list.generate_sample_sort, "title": "List sort"},
        {"func": time_comparison_list.generate_sample_in, "title": "List in"}
    ]
    print("================List Sample================")
    for sample in list_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])

    # Set
    set_samples = [
        {"func": time_comparison_set.generate_sample_clear, "title": "Set clear"},
        {"func": time_comparison_set.generate_sample_copy, "title": "Set copy"},
        {"func": time_comparison_set.generate_sample_remove, "title": "Set remove"},
        {"func": time_comparison_set.generate_sample_in, "title": "Set in"},
        {"func": time_comparison_set.generate_sample_add, "title": "Set in"}
    ]

    print("================Set Sample================")
    for sample in set_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])

    # Repeated character
    print("================Repeated character Sample================")
    print("Sample for {} generated".format("Repeated Characte"))
    graph_men_and_time(generate_repeated_character(), "Repeated Character")


if __name__ == '__main__':
    main()
