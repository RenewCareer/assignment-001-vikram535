"""
Tests for Part 1 — Variables & Data Types
==========================================
Run with:  pytest tests/test_python_basics.py -v
"""

import pytest
import sys
import os

# Make the starter package importable regardless of working directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from starter.python_basics import (
    create_student_info,
    convert_temperature,
    classify_number,
    format_greeting,
    calculate_bmi,
    safe_divide,
)


# ===========================================================================
# Exercise 1 — create_student_info
# ===========================================================================
class TestCreateStudentInfo:
    def test_returns_dict(self):
        result = create_student_info("Alice", 20, 3.756)
        assert isinstance(result, dict)

    def test_keys_present(self):
        result = create_student_info("Alice", 20, 3.756)
        assert set(result.keys()) == {"name", "age", "gpa", "is_passing"}

    def test_name_stripped(self):
        result = create_student_info("  Alice  ", 20, 3.0)
        assert result["name"] == "Alice"

    def test_name_type(self):
        result = create_student_info("Alice", 20, 3.0)
        assert isinstance(result["name"], str)

    def test_age_type(self):
        result = create_student_info("Alice", 20, 3.0)
        assert isinstance(result["age"], int)
        assert result["age"] == 20

    def test_gpa_rounded(self):
        result = create_student_info("Alice", 20, 3.756)
        assert result["gpa"] == 3.76

    def test_gpa_type(self):
        result = create_student_info("Alice", 20, 3.0)
        assert isinstance(result["gpa"], float)

    def test_is_passing_true(self):
        result = create_student_info("Alice", 20, 2.0)
        assert result["is_passing"] is True

    def test_is_passing_false(self):
        result = create_student_info("Bob", 17, 1.5)
        assert result["is_passing"] is False

    def test_is_passing_exactly_2(self):
        result = create_student_info("Carol", 22, 2.0)
        assert result["is_passing"] is True

    def test_full_example(self):
        result = create_student_info("  Bob  ", 17, 1.5)
        assert result == {"name": "Bob", "age": 17, "gpa": 1.5, "is_passing": False}


# ===========================================================================
# Exercise 2 — convert_temperature
# ===========================================================================
class TestConvertTemperature:
    def test_returns_dict(self):
        assert isinstance(convert_temperature(0), dict)

    def test_keys_present(self):
        result = convert_temperature(0)
        assert set(result.keys()) == {"celsius", "fahrenheit", "kelvin"}

    def test_freezing_point(self):
        result = convert_temperature(0)
        assert result == {"celsius": 0.0, "fahrenheit": 32.0, "kelvin": 273.15}

    def test_boiling_point(self):
        result = convert_temperature(100)
        assert result == {"celsius": 100.0, "fahrenheit": 212.0, "kelvin": 373.15}

    def test_body_temperature(self):
        result = convert_temperature(37)
        assert result["fahrenheit"] == 98.6
        assert result["kelvin"] == 310.15

    def test_negative_celsius(self):
        result = convert_temperature(-40)
        assert result["fahrenheit"] == -40.0

    def test_values_are_floats(self):
        result = convert_temperature(25)
        assert isinstance(result["celsius"], float)
        assert isinstance(result["fahrenheit"], float)
        assert isinstance(result["kelvin"], float)

    def test_rounding(self):
        result = convert_temperature(37.5)
        assert result["fahrenheit"] == round((37.5 * 9 / 5) + 32, 2)


# ===========================================================================
# Exercise 3 — classify_number
# ===========================================================================
class TestClassifyNumber:
    def test_positive_even(self):
        assert classify_number(4) == "positive even"

    def test_positive_odd(self):
        assert classify_number(7) == "positive odd"

    def test_negative_even(self):
        assert classify_number(-8) == "negative even"

    def test_negative_odd(self):
        assert classify_number(-3) == "negative odd"

    def test_zero(self):
        assert classify_number(0) == "zero"

    def test_large_positive_even(self):
        assert classify_number(100) == "positive even"

    def test_large_negative_odd(self):
        assert classify_number(-101) == "negative odd"

    def test_float_treated_as_odd(self):
        assert classify_number(3.5) == "positive odd"


# ===========================================================================
# Exercise 4 — format_greeting
# ===========================================================================
class TestFormatGreeting:
    def test_default_english(self):
        assert format_greeting("alice") == "Hello, Alice!"

    def test_explicit_english(self):
        assert format_greeting("bob", "english") == "Hello, Bob!"

    def test_spanish(self):
        assert format_greeting("alice", "spanish") == "¡Hola, Alice!"

    def test_french(self):
        assert format_greeting("alice", "french") == "Bonjour, Alice!"

    def test_german(self):
        assert format_greeting("alice", "german") == "Hallo, Alice!"

    def test_swahili(self):
        assert format_greeting("alice", "swahili") == "Habari, Alice!"

    def test_case_insensitive_language(self):
        assert format_greeting("alice", "SPANISH") == "¡Hola, Alice!"

    def test_name_title_cased(self):
        result = format_greeting("john doe", "english")
        assert result == "Hello, John Doe!"

    def test_unknown_language_falls_back_to_english(self):
        assert format_greeting("alice", "klingon") == "Hello, Alice!"


# ===========================================================================
# Exercise 5 — calculate_bmi
# ===========================================================================
class TestCalculateBMI:
    def test_returns_dict(self):
        assert isinstance(calculate_bmi(70, 1.75), dict)

    def test_keys_present(self):
        result = calculate_bmi(70, 1.75)
        assert set(result.keys()) == {"bmi", "category"}

    def test_normal_weight(self):
        result = calculate_bmi(70, 1.75)
        assert result["bmi"] == 22.9
        assert result["category"] == "Normal weight"

    def test_underweight(self):
        result = calculate_bmi(45, 1.75)
        assert result["category"] == "Underweight"

    def test_overweight(self):
        result = calculate_bmi(80, 1.70)
        assert result["category"] == "Overweight"

    def test_obese(self):
        result = calculate_bmi(120, 1.70)
        assert result["category"] == "Obese"

    def test_bmi_rounded_to_1_dp(self):
        result = calculate_bmi(70, 1.75)
        assert result["bmi"] == round(70 / (1.75 ** 2), 1)

    def test_raises_on_zero_height(self):
        with pytest.raises(ValueError, match="Height must be positive"):
            calculate_bmi(70, 0)

    def test_raises_on_negative_height(self):
        with pytest.raises(ValueError, match="Height must be positive"):
            calculate_bmi(70, -1)

    def test_raises_on_zero_weight(self):
        with pytest.raises(ValueError, match="Weight must be positive"):
            calculate_bmi(0, 1.75)


# ===========================================================================
# Exercise 6 — safe_divide
# ===========================================================================
class TestSafeDivide:
    def test_exact_division(self):
        assert safe_divide(10, 2) == "5.0000"

    def test_four_decimal_places(self):
        assert safe_divide(10, 3) == "3.3333"

    def test_zero_denominator(self):
        assert safe_divide(7, 0) == "Error: division by zero"

    def test_returns_string(self):
        assert isinstance(safe_divide(10, 4), str)

    def test_half(self):
        assert safe_divide(5, 2) == "2.5000"

    def test_negative_numerator(self):
        assert safe_divide(-10, 4) == "-2.5000"

    def test_both_negative(self):
        assert safe_divide(-6, -2) == "3.0000"

    def test_zero_numerator(self):
        assert safe_divide(0, 5) == "0.0000"
