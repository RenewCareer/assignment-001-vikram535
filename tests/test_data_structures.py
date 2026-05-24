"""
Tests for Part 2 — Data Structures
=====================================
Run with:  pytest tests/test_data_structures.py -v
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from starter.data_structures import (
    get_unique_sorted,
    merge_and_sort,
    count_word_frequency,
    get_top_n,
    flatten_one_level,
    invert_dictionary,
    common_elements,
    group_by_first_letter,
)


# ===========================================================================
# Exercise 1 — get_unique_sorted
# ===========================================================================
class TestGetUniqueSorted:
    def test_basic_numbers(self):
        assert get_unique_sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 2, 3, 4, 5, 6, 9]

    def test_strings(self):
        assert get_unique_sorted(["banana", "apple", "apple", "cherry"]) == [
            "apple", "banana", "cherry"
        ]

    def test_already_unique(self):
        assert get_unique_sorted([5, 3, 1]) == [1, 3, 5]

    def test_empty_list(self):
        assert get_unique_sorted([]) == []

    def test_single_element(self):
        assert get_unique_sorted([42]) == [42]

    def test_all_duplicates(self):
        assert get_unique_sorted([7, 7, 7, 7]) == [7]

    def test_returns_list(self):
        assert isinstance(get_unique_sorted([1, 2]), list)


# ===========================================================================
# Exercise 2 — merge_and_sort
# ===========================================================================
class TestMergeAndSort:
    def test_basic_merge(self):
        assert merge_and_sort([3, 1, 4], [1, 5, 9]) == [1, 1, 3, 4, 5, 9]

    def test_keeps_duplicates(self):
        result = merge_and_sort([1, 2], [1, 2])
        assert result == [1, 1, 2, 2]

    def test_empty_first(self):
        assert merge_and_sort([], [7, 2]) == [2, 7]

    def test_empty_second(self):
        assert merge_and_sort([7, 2], []) == [2, 7]

    def test_both_empty(self):
        assert merge_and_sort([], []) == []

    def test_returns_list(self):
        assert isinstance(merge_and_sort([1], [2]), list)

    def test_single_elements(self):
        assert merge_and_sort([5], [3]) == [3, 5]


# ===========================================================================
# Exercise 3 — count_word_frequency
# ===========================================================================
class TestCountWordFrequency:
    def test_basic_sentence(self):
        result = count_word_frequency("the cat sat on the mat")
        assert result == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

    def test_case_insensitive(self):
        result = count_word_frequency("Hello hello HELLO")
        assert result == {"hello": 3}

    def test_empty_string(self):
        assert count_word_frequency("") == {}

    def test_single_word(self):
        assert count_word_frequency("python") == {"python": 1}

    def test_returns_dict(self):
        assert isinstance(count_word_frequency("a b c"), dict)

    def test_preserves_punctuation(self):
        result = count_word_frequency("hello, hello")
        # "hello," and "hello" are different words
        assert "hello," in result
        assert "hello" in result

    def test_mixed_case_counted_once(self):
        result = count_word_frequency("Cat CAT cat")
        assert result.get("cat") == 3


# ===========================================================================
# Exercise 4 — get_top_n
# ===========================================================================
class TestGetTopN:
    def test_basic(self):
        d = {"apple": 5, "banana": 3, "cherry": 5, "date": 1}
        assert get_top_n(d, 2) == ["apple", "cherry"]

    def test_n_larger_than_dict(self):
        d = {"a": 2, "b": 2}
        result = get_top_n(d, 5)
        assert sorted(result) == ["a", "b"]

    def test_n_equals_dict_size(self):
        d = {"a": 3, "b": 1, "c": 2}
        assert get_top_n(d, 3) == ["a", "c", "b"]

    def test_returns_list(self):
        assert isinstance(get_top_n({"a": 1}, 1), list)

    def test_top_1(self):
        d = {"x": 10, "y": 5, "z": 8}
        assert get_top_n(d, 1) == ["x"]

    def test_alphabetical_tiebreak(self):
        d = {"banana": 3, "apple": 3, "cherry": 3}
        result = get_top_n(d, 3)
        assert result == ["apple", "banana", "cherry"]

    def test_empty_dict(self):
        assert get_top_n({}, 3) == []


# ===========================================================================
# Exercise 5 — flatten_one_level
# ===========================================================================
class TestFlattenOneLevel:
    def test_basic(self):
        assert flatten_one_level([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

    def test_preserves_deep_nesting(self):
        assert flatten_one_level([[1, [2, 3]], [4]]) == [1, [2, 3], 4]

    def test_empty_input(self):
        assert flatten_one_level([]) == []

    def test_empty_sublists(self):
        assert flatten_one_level([[], [1, 2], []]) == [1, 2]

    def test_single_sublist(self):
        assert flatten_one_level([[10, 20, 30]]) == [10, 20, 30]

    def test_returns_list(self):
        assert isinstance(flatten_one_level([[1]]), list)

    def test_strings_flattened(self):
        assert flatten_one_level([["a", "b"], ["c"]]) == ["a", "b", "c"]


# ===========================================================================
# Exercise 6 — invert_dictionary
# ===========================================================================
class TestInvertDictionary:
    def test_basic(self):
        assert invert_dictionary({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}

    def test_empty(self):
        assert invert_dictionary({}) == {}

    def test_returns_dict(self):
        assert isinstance(invert_dictionary({"x": 99}), dict)

    def test_single_pair(self):
        assert invert_dictionary({"hello": "world"}) == {"world": "hello"}

    def test_integer_keys_become_values(self):
        result = invert_dictionary({1: "one", 2: "two"})
        assert result == {"one": 1, "two": 2}

    def test_no_mutation_of_input(self):
        original = {"a": 1}
        invert_dictionary(original)
        assert original == {"a": 1}


# ===========================================================================
# Exercise 7 — common_elements
# ===========================================================================
class TestCommonElements:
    def test_basic_numbers(self):
        assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    def test_no_common(self):
        assert common_elements([1, 2], [3, 4]) == []

    def test_strings(self):
        assert common_elements(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]

    def test_all_common(self):
        assert common_elements([1, 2, 3], [3, 1, 2]) == [1, 2, 3]

    def test_empty_lists(self):
        assert common_elements([], [1, 2]) == []

    def test_returns_sorted_list(self):
        result = common_elements([5, 1, 3], [3, 5, 7])
        assert result == sorted(result)

    def test_returns_list(self):
        assert isinstance(common_elements([1], [1]), list)

    def test_duplicates_handled(self):
        # Even if input has duplicates, each common element appears once
        assert common_elements([1, 1, 2], [1, 2, 2]) == [1, 2]


# ===========================================================================
# Exercise 8 — group_by_first_letter
# ===========================================================================
class TestGroupByFirstLetter:
    def test_basic(self):
        result = group_by_first_letter(["Apple", "ant", "Banana", "avocado"])
        assert result == {"a": ["Apple", "ant", "avocado"], "b": ["Banana"]}

    def test_empty_list(self):
        assert group_by_first_letter([]) == {}

    def test_empty_strings_ignored(self):
        result = group_by_first_letter(["", "apple", ""])
        assert "" not in result
        assert "a" in result

    def test_returns_dict(self):
        assert isinstance(group_by_first_letter(["a"]), dict)

    def test_values_are_sorted(self):
        result = group_by_first_letter(["cherry", "carrot", "cabbage"])
        assert result["c"] == sorted(["cherry", "carrot", "cabbage"])

    def test_keys_are_lowercase(self):
        result = group_by_first_letter(["Apple", "Avocado"])
        assert "a" in result
        assert "A" not in result

    def test_case_insensitive_grouping(self):
        result = group_by_first_letter(["Ant", "apple"])
        assert len(result) == 1
        assert "a" in result
        assert set(result["a"]) == {"Ant", "apple"}

    def test_single_word(self):
        assert group_by_first_letter(["Python"]) == {"p": ["Python"]}
