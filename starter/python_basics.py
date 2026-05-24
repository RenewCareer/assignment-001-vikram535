"""
Part 1 — Variables & Data Types
================================
Implement each function below according to its docstring.

Rules:
  - Do NOT rename functions or change their signatures.
  - Do NOT import any third-party libraries (the standard library is fine).
  - Remove the `pass` statement and replace it with your implementation.

Run your tests with:
    pytest tests/test_python_basics.py -v
"""


# ---------------------------------------------------------------------------
# Exercise 1  (5 pts)
# ---------------------------------------------------------------------------

def create_student_info(name: str, age: int, gpa: float) -> dict:
    """Return a dictionary with student information and correct types.

    The returned dictionary must contain exactly these keys:
        "name"  -> str   : the student's name (stripped of leading/trailing spaces)
        "age"   -> int   : the student's age
        "gpa"   -> float : the GPA rounded to 2 decimal places
        "is_passing" -> bool : True if gpa >= 2.0, otherwise False

    Examples:
        >>> create_student_info("Alice", 20, 3.756)
        {'name': 'Alice', 'age': 20, 'gpa': 3.76, 'is_passing': True}

        >>> create_student_info("  Bob  ", 17, 1.5)
        {'name': 'Bob', 'age': 17, 'gpa': 1.5, 'is_passing': False}
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 2  (5 pts)
# ---------------------------------------------------------------------------

def convert_temperature(celsius: float) -> dict:
    """Convert a temperature from Celsius to Fahrenheit and Kelvin.

    Return a dictionary with three keys:
        "celsius"    -> float : the original value rounded to 2 dp
        "fahrenheit" -> float : (celsius * 9/5) + 32, rounded to 2 dp
        "kelvin"     -> float : celsius + 273.15, rounded to 2 dp

    Examples:
        >>> convert_temperature(0)
        {'celsius': 0.0, 'fahrenheit': 32.0, 'kelvin': 273.15}

        >>> convert_temperature(100)
        {'celsius': 100.0, 'fahrenheit': 212.0, 'kelvin': 373.15}
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 3  (5 pts)
# ---------------------------------------------------------------------------

def classify_number(n: float) -> str:
    """Classify a number and return a descriptive string.

    Return exactly one of:
        "positive even"   – n > 0 and divisible by 2
        "positive odd"    – n > 0 and NOT divisible by 2
        "negative even"   – n < 0 and divisible by 2  (use abs for divisibility)
        "negative odd"    – n < 0 and NOT divisible by 2
        "zero"            – n == 0

    Note: for non-integer floats (e.g. 3.5) treat them as odd.

    Examples:
        >>> classify_number(4)
        'positive even'
        >>> classify_number(-7)
        'negative odd'
        >>> classify_number(0)
        'zero'
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 4  (5 pts)
# ---------------------------------------------------------------------------

def format_greeting(name: str, language: str = "english") -> str:
    """Return a personalised greeting in the requested language.

    Supported languages (case-insensitive):
        "english"  -> "Hello, <name>!"
        "spanish"  -> "¡Hola, <name>!"
        "french"   -> "Bonjour, <name>!"
        "german"   -> "Hallo, <name>!"
        "swahili"  -> "Habari, <name>!"
        any other  -> "Hello, <name>!"   (fall back to English)

    The name should be title-cased in the output.

    Examples:
        >>> format_greeting("alice", "spanish")
        '¡Hola, Alice!'
        >>> format_greeting("bob")
        'Hello, Bob!'
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 5  (5 pts)
# ---------------------------------------------------------------------------

def calculate_bmi(weight_kg: float, height_m: float) -> dict:
    """Calculate Body Mass Index (BMI) and return a result dictionary.

    Formula: bmi = weight_kg / (height_m ** 2)

    BMI categories (use these exact strings):
        bmi < 18.5             -> "Underweight"
        18.5 <= bmi < 25.0     -> "Normal weight"
        25.0 <= bmi < 30.0     -> "Overweight"
        bmi >= 30.0            -> "Obese"

    Return a dict with:
        "bmi"      -> float  : rounded to 1 decimal place
        "category" -> str    : one of the four strings above

    Raise ValueError with message "Height must be positive" if height_m <= 0.
    Raise ValueError with message "Weight must be positive" if weight_kg <= 0.

    Examples:
        >>> calculate_bmi(70, 1.75)
        {'bmi': 22.9, 'category': 'Normal weight'}
    """
    pass  # TODO: implement this function


# ---------------------------------------------------------------------------
# Exercise 6  (5 pts)
# ---------------------------------------------------------------------------

def safe_divide(numerator: float, denominator: float) -> str:
    """Safely divide two numbers and return the result as a formatted string.

    If denominator is 0, return the string "Error: division by zero".
    Otherwise return the result formatted to exactly 4 decimal places
    as a string, e.g. "3.3333" or "2.5000".

    Examples:
        >>> safe_divide(10, 3)
        '3.3333'
        >>> safe_divide(5, 2)
        '2.5000'
        >>> safe_divide(7, 0)
        'Error: division by zero'
    """
    pass  # TODO: implement this function
