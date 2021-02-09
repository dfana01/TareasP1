import time_comparison_double_linked_list
from util import graph_men_and_time


def main():
    # List
    list_samples = [
        {"func": time_comparison_double_linked_list.generate_sample_add, "title": "List Add"},
        {"func": time_comparison_double_linked_list.generate_sample_clear, "title": "List Clear"},
        {"func": time_comparison_double_linked_list.generate_sample_clone, "title": "List Clone"},
        {"func": time_comparison_double_linked_list.generate_sample_index_start, "title": "List Index Start"},
        {"func": time_comparison_double_linked_list.generate_sample_index_middle, "title": "List Index Middle"},
        {"func": time_comparison_double_linked_list.generate_sample_index_end, "title": "List Index End"},
        {"func": time_comparison_double_linked_list.generate_sample_add_index_start, "title": "List Add Index Start"},
        {"func": time_comparison_double_linked_list.generate_sample_add_index_middle, "title": "List Add Index Middle"},
        {"func": time_comparison_double_linked_list.generate_sample_add_index_end, "title": "List Add Index End"},
        {"func": time_comparison_double_linked_list.generate_sample_remove_start, "title": "List Remove Start"},
        {"func": time_comparison_double_linked_list.generate_sample_remove_middle, "title": "List Remove Middle"},
        {"func": time_comparison_double_linked_list.generate_sample_remove_end, "title": "List Remove End"},
        {"func": time_comparison_double_linked_list.generate_sample_in_start, "title": "List In Start"},
        {"func": time_comparison_double_linked_list.generate_sample_in_middle, "title": "List In Middle"},
        {"func": time_comparison_double_linked_list.generate_sample_in_end, "title": "List In End"},
        {"func": time_comparison_double_linked_list.generate_sample_add_all, "title": "List Add All"},
        {"func": time_comparison_double_linked_list.generate_sample_get_start, "title": "List Get Start"},
        {"func": time_comparison_double_linked_list.generate_sample_get_middle, "title": "List Get Middle"},
        {"func": time_comparison_double_linked_list.generate_sample_get_end, "title": "List Get End"},
    ]
    print("================List Sample================")
    for sample in list_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])


if __name__ == '__main__':
    main()
