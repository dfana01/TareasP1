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
        {"func": time_comparison_list.generate_sample_insert_start, "title": "List insert start"},
        {"func": time_comparison_list.generate_sample_insert_middle, "title": "List insert middle"},
        {"func": time_comparison_list.generate_sample_insert_end, "title": "List insert end"},
        {"func": time_comparison_list.generate_sample_remove_start, "title": "List remove start"},
        {"func": time_comparison_list.generate_sample_remove_middle, "title": "List remove middle"},
        {"func": time_comparison_list.generate_sample_remove_end, "title": "List remove end"},
        {"func": time_comparison_list.generate_sample_sort, "title": "List sort"},
        {"func": time_comparison_list.generate_sample_in_start, "title": "List in start"},
        {"func": time_comparison_list.generate_sample_in_middle, "title": "List in middle"},
        {"func": time_comparison_list.generate_sample_in_end, "title": "List in end"}
    ]
    print("================List Sample================")
    for sample in list_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])

    # Set
    set_samples = [
        {"func": time_comparison_set.generate_sample_clear, "title": "Set clear"},
        {"func": time_comparison_set.generate_sample_copy, "title": "Set copy"},
        {"func": time_comparison_set.generate_sample_remove_start, "title": "Set remove start"},
        {"func": time_comparison_set.generate_sample_remove_middle, "title": "Set remove middle"},
        {"func": time_comparison_set.generate_sample_remove_end, "title": "Set remove end"},
        {"func": time_comparison_set.generate_sample_in_start, "title": "Set in start"},
        {"func": time_comparison_set.generate_sample_in_middle, "title": "Set in middle"},
        {"func": time_comparison_set.generate_sample_in_end, "title": "Set in end"},
        {"func": time_comparison_set.generate_sample_add, "title": "Set add"}
    ]

    print("================Set Sample================")
    for sample in set_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])

    # Repeated character
    print("================Repeated character Sample================")
    print("Sample for {} generated".format("Repeated Characters"))
    graph_men_and_time(generate_repeated_character(), "Repeated Character")


if __name__ == '__main__':
    main()
