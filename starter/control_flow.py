"""
Part 3 — Control Flow
======================
Implement each function below according to its docstring.

Rules:
  - Do NOT rename functions or change their signatures.
  - Do NOT import any third-party libraries (the standard library is fine).
  - Remove the `pass` statement and replace it with your implementation.

Run your tests with:
    pytest tests/test_control_flow.py -v
"""


# ---------------------------------------------------------------------------
# Exercise 1  (5 pts)  — if / elif / else
# ---------------------------------------------------------------------------

def grade_calculator(score: float) -> str:
    """Convert a numeric score (0–100) to a letter grade.

    Grading scale:
        90 – 100  ->  "A"
        80 – 89   ->  "B"
        70 – 79   ->  "C"
        60 – 69   ->  "D"
         0 – 59   ->  "F"

    Raise ValueError with message "Score must be between 0 and 100"
    if score < 0 or score > 100.

    Examples:
        >>> grade_calculator(95)
        'A'
        >>> grade_calculator(72)
        'C'
        >>> grade_calculator(55)
        'F'
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 2  (5 pts)  — for loop / if
# ---------------------------------------------------------------------------

def fizzbuzz(n: int) -> list:
    """Return a list of FizzBuzz results for numbers 1 through n (inclusive).

    Rules:
        - Replace multiples of 3 with "Fizz"
        - Replace multiples of 5 with "Buzz"
        - Replace multiples of both 3 AND 5 with "FizzBuzz"
        - All other numbers appear as integers (not strings)

    Raise ValueError with message "n must be a positive integer" if n < 1.

    Examples:
        >>> fizzbuzz(15)
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
         11, 'Fizz', 13, 14, 'FizzBuzz']
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 3  (5 pts)  — for loop / list comprehension
# ---------------------------------------------------------------------------

def sum_of_evens(numbers: list) -> int:
    """Return the sum of all even integers in *numbers*.

    Non-integer values in the list are ignored.
    An empty list returns 0.

    Examples:
        >>> sum_of_evens([1, 2, 3, 4, 5, 6])
        12
        >>> sum_of_evens([1, 3, 5])
        0
        >>> sum_of_evens([1, "hello", 4, None, 6])
        10
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 4  (5 pts)  — while loop / math
# ---------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number, False otherwise.

    By definition:
        - Numbers less than 2 are NOT prime.
        - 2 is prime.
        - Any number divisible only by 1 and itself is prime.

    Hint: you only need to check divisors up to sqrt(n).

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
        >>> is_prime(15)
        False
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 5  (5 pts)  — for loop + is_prime
# ---------------------------------------------------------------------------

def find_primes(limit: int) -> list:
    """Return a list of all prime numbers up to and including *limit*.

    Use your `is_prime` function from Exercise 4.
    Return an empty list if limit < 2.

    Examples:
        >>> find_primes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        >>> find_primes(1)
        []
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 6  (5 pts)  — while loop
# ---------------------------------------------------------------------------

def collatz_length(n: int) -> int:
    """Return the number of steps to reach 1 using the Collatz sequence.

    Collatz rules (applied repeatedly until n == 1):
        If n is even  ->  n = n // 2
        If n is odd   ->  n = 3 * n + 1

    The starting number counts as step 1; reaching 1 is the final step.

    Raise ValueError with message "n must be a positive integer" if n < 1.

    Examples:
        >>> collatz_length(1)
        1
        >>> collatz_length(6)
        9    # sequence: 6, 3, 10, 5, 16, 8, 4, 2, 1
        >>> collatz_length(27)
        112
    """
    pass  # TODO: implement this function
