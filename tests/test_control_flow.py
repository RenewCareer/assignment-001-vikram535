"""
Tests for Part 3 — Control Flow
=================================
Run with:  pytest tests/test_control_flow.py -v
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from starter.control_flow import (
    grade_calculator,
    fizzbuzz,
    sum_of_evens,
    is_prime,
    find_primes,
    collatz_length,
)


# ===========================================================================
# Exercise 1 — grade_calculator
# ===========================================================================
class TestGradeCalculator:
    def test_a_grade(self):
        assert grade_calculator(95) == "A"

    def test_a_grade_boundary(self):
        assert grade_calculator(90) == "A"

    def test_b_grade(self):
        assert grade_calculator(85) == "B"

    def test_b_grade_boundary(self):
        assert grade_calculator(80) == "B"

    def test_c_grade(self):
        assert grade_calculator(72) == "C"

    def test_c_grade_boundary(self):
        assert grade_calculator(70) == "C"

    def test_d_grade(self):
        assert grade_calculator(65) == "D"

    def test_d_grade_boundary(self):
        assert grade_calculator(60) == "D"

    def test_f_grade(self):
        assert grade_calculator(55) == "F"

    def test_f_grade_zero(self):
        assert grade_calculator(0) == "F"

    def test_perfect_score(self):
        assert grade_calculator(100) == "A"

    def test_raises_above_100(self):
        with pytest.raises(ValueError, match="Score must be between 0 and 100"):
            grade_calculator(101)

    def test_raises_below_0(self):
        with pytest.raises(ValueError, match="Score must be between 0 and 100"):
            grade_calculator(-1)


# ===========================================================================
# Exercise 2 — fizzbuzz
# ===========================================================================
class TestFizzBuzz:
    def test_returns_list(self):
        assert isinstance(fizzbuzz(5), list)

    def test_length(self):
        assert len(fizzbuzz(10)) == 10

    def test_fizz(self):
        result = fizzbuzz(3)
        assert result[2] == "Fizz"

    def test_buzz(self):
        result = fizzbuzz(5)
        assert result[4] == "Buzz"

    def test_fizzbuzz_15(self):
        result = fizzbuzz(15)
        assert result[14] == "FizzBuzz"

    def test_numbers_are_ints(self):
        result = fizzbuzz(5)
        assert result[0] == 1  # integer
        assert isinstance(result[0], int)

    def test_full_15(self):
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
                    11, "Fizz", 13, 14, "FizzBuzz"]
        assert fizzbuzz(15) == expected

    def test_n_equals_1(self):
        assert fizzbuzz(1) == [1]

    def test_raises_on_zero(self):
        with pytest.raises(ValueError, match="n must be a positive integer"):
            fizzbuzz(0)

    def test_raises_on_negative(self):
        with pytest.raises(ValueError, match="n must be a positive integer"):
            fizzbuzz(-5)


# ===========================================================================
# Exercise 3 — sum_of_evens
# ===========================================================================
class TestSumOfEvens:
    def test_basic(self):
        assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12

    def test_no_evens(self):
        assert sum_of_evens([1, 3, 5]) == 0

    def test_empty_list(self):
        assert sum_of_evens([]) == 0

    def test_ignores_strings(self):
        assert sum_of_evens([1, "hello", 4, None, 6]) == 10

    def test_ignores_floats(self):
        # floats are not integers; they are ignored
        assert sum_of_evens([2.0, 4, 6]) == 10

    def test_negative_evens_counted(self):
        assert sum_of_evens([-2, -4, 1]) == -6

    def test_returns_int(self):
        assert isinstance(sum_of_evens([2, 4]), int)

    def test_all_even(self):
        assert sum_of_evens([2, 4, 6, 8]) == 20


# ===========================================================================
# Exercise 4 — is_prime
# ===========================================================================
class TestIsPrime:
    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_three_is_prime(self):
        assert is_prime(3) is True

    def test_one_is_not_prime(self):
        assert is_prime(1) is False

    def test_zero_is_not_prime(self):
        assert is_prime(0) is False

    def test_negative_is_not_prime(self):
        assert is_prime(-5) is False

    def test_4_is_not_prime(self):
        assert is_prime(4) is False

    def test_17_is_prime(self):
        assert is_prime(17) is True

    def test_15_is_not_prime(self):
        assert is_prime(15) is False

    def test_97_is_prime(self):
        assert is_prime(97) is True

    def test_100_is_not_prime(self):
        assert is_prime(100) is False

    def test_returns_bool(self):
        assert isinstance(is_prime(7), bool)


# ===========================================================================
# Exercise 5 — find_primes
# ===========================================================================
class TestFindPrimes:
    def test_primes_up_to_20(self):
        assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_limit_is_prime(self):
        # 19 is prime, should be included
        assert 19 in find_primes(19)

    def test_limit_1_returns_empty(self):
        assert find_primes(1) == []

    def test_limit_0_returns_empty(self):
        assert find_primes(0) == []

    def test_limit_2(self):
        assert find_primes(2) == [2]

    def test_returns_list(self):
        assert isinstance(find_primes(10), list)

    def test_no_composites(self):
        result = find_primes(30)
        assert all(is_prime(n) for n in result)

    def test_primes_up_to_50(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        assert find_primes(50) == expected


# ===========================================================================
# Exercise 6 — collatz_length
# ===========================================================================
class TestCollatzLength:
    def test_n_equals_1(self):
        assert collatz_length(1) == 1

    def test_n_equals_2(self):
        # 2 -> 1 : 2 steps
        assert collatz_length(2) == 2

    def test_n_equals_6(self):
        # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 : 9 steps
        assert collatz_length(6) == 9

    def test_n_equals_27(self):
        assert collatz_length(27) == 112

    def test_n_equals_4(self):
        # 4 -> 2 -> 1 : 3 steps
        assert collatz_length(4) == 3

    def test_returns_int(self):
        assert isinstance(collatz_length(5), int)

    def test_raises_on_zero(self):
        with pytest.raises(ValueError, match="n must be a positive integer"):
            collatz_length(0)

    def test_raises_on_negative(self):
        with pytest.raises(ValueError, match="n must be a positive integer"):
            collatz_length(-3)

    def test_large_n(self):
        # Should complete without recursion depth errors
        result = collatz_length(1000)
        assert isinstance(result, int)
        assert result > 0
