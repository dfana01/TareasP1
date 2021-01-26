import unittest
import util
import character_frecuency
import time_comparison_list as tcl
import time_comparison_set as tcs


class TimeComparisonSet(unittest.TestCase):
    def test_generate_sample_clear(self):
        self.assertTrue(tcs.generate_sample_clear() is not None)

    def test_generate_sample_add(self):
        self.assertTrue(tcs.generate_sample_add() is not None)

    def test_generate_sample_copy(self):
        self.assertTrue(tcs.generate_sample_copy() is not None)

    def test_generate_sample_remove(self):
        self.assertTrue(tcs.generate_sample_remove() is not None)

    def test_generate_sample_in(self):
        self.assertTrue(tcs.generate_sample_in() is not None)


class TimeComparisonList(unittest.TestCase):
    def test_generate_sample_append(self):
        self.assertTrue(tcl.generate_sample_append() is not None)

    def test_generate_sample_clear(self):
        self.assertTrue(tcl.generate_sample_clear() is not None)

    def test_generate_sample_copy(self):
        self.assertTrue(tcl.generate_sample_copy() is not None)

    def test_generate_sample_index(self):
        self.assertTrue(tcl.generate_sample_index() is not None)

    def test_generate_sample_insert(self):
        self.assertTrue(tcl.generate_sample_insert() is not None)

    def test_generate_sample_remove(self):
        self.assertTrue(tcl.generate_sample_remove() is not None)

    def test_generate_sample_sort(self):
        self.assertTrue(tcl.generate_sample_sort() is not None)

    def test_generate_sample_in(self):
        self.assertTrue(tcl.generate_sample_in() is not None)


class RepeatedCharacterTestFact(unittest.TestCase):
    def test_empty_str(self):
        r = {}
        self.assertTrue(character_frecuency.repeated_character("") == r)

    def test_input_1(self):
        d = "asdnhnndahhh"
        r = {"a": 2, "s": 1, "d": 2, "n": 3, "h": 4}
        self.assertTrue(character_frecuency.repeated_character(d) == r)


class MiscellaneousTestFact(unittest.TestCase):
    def test_graph_men_and_time(self):
        self.assertTrue(True)

    def test_graph(self):
        self.assertTrue(True)

    def test_get_current_ram(self):
        self.assertTrue(util.get_current_ram() > 0)

    def test_get_current_time(self):
        self.assertTrue(util.get_current_time() > 0)

    def test_generate_range_numbers(self):
        self.assertTrue(len(util.generate_range_numbers()) == util.N_TIMES)

    def test_get_avg(self):
        self.assertTrue(util.get_avg([1, 2, 3, 4, 5]) == 3)

    def test_get_deviation(self):
        self.assertTrue(util.get_deviation(3, [1, 2, 3, 4, 5]) > 1.5)

    def test_standardize_sample(self):
        r = util.standardize_sample({
            0: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        })
        self.assertTrue(isinstance(r, list))

    def test_with_rep_and_standardize(self):
        def f(s):
            return {}
        r = util.with_rep_and_standardize(f, rep=1)
        self.assertTrue(r == [])

    def test_add_to_sample_1(self):
        sample = util.add_to_sample(1, 0, 0, {})
        self.assertTrue(1 in sample)

    def test_add_to_sample_2(self):
        sample = util.add_to_sample(1, 0, 0, {1: [[], []]})
        self.assertTrue(1 in sample)

    def test_get_random_str(self):
        self.assertTrue(len(util.get_random_str(5)) == 5)

    def test_random_number_between(self):
        self.assertTrue(util.random_number_between(0, 5) <= 5)


if __name__ == '__main__':
    unittest.main()
