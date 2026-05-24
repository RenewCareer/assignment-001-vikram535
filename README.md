# Assignment 1 — Python Basics & GitHub Fundamentals

> **Course:** Introduction to Generative AI with Python  
> **Points:** 100 (30 + 40 + 30)  
> **Due:** Check your GitHub Classroom invitation for the deadline

---

## 🎯 Learning Objectives

By completing this assignment you will be able to:

| Skill | Topic |
|-------|-------|
| ✅ | Clone a repository, commit changes, and push to GitHub |
| ✅ | Declare and use Python variables with correct data types |
| ✅ | Work with lists, dictionaries, tuples, and sets |
| ✅ | Write `if/elif/else`, `for`, and `while` control-flow structures |
| ✅ | Run a test suite locally with `pytest` |

---

## 📁 Repository Layout

```
Assignment_1/
├── README.md                         ← you are here
├── requirements.txt                  ← Python dependencies
├── starter/
│   ├── python_basics.py              ← Part 1  (30 pts)
│   ├── data_structures.py            ← Part 2  (40 pts)
│   └── control_flow.py               ← Part 3  (30 pts)
└── tests/
    ├── test_python_basics.py
    ├── test_data_structures.py
    └── test_control_flow.py
```

---

## 🚀 Getting Started

### 1 — Accept the Assignment
Click the GitHub Classroom link shared by your instructor. This creates your own private copy of the repository.

### 2 — Clone Your Repo
```bash
git clone <your-classroom-repo-url>
cd Assignment_1
```

### 3 — Set Up Your Python Environment
```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4 — Work on the Starter Files
Open the files inside `starter/` and implement each function. Every function has a docstring describing what it should do — **do not change function signatures or file names**.

### 5 — Run Tests Locally Before Pushing
```bash
# Run all tests
pytest tests/ -v

# Run a single test file
pytest tests/test_python_basics.py -v

# See a coverage summary
pytest tests/ --tb=short
```

### 6 — Commit and Push
```bash
git add starter/
git commit -m "Complete Part 1: python basics"
git push
```

GitHub Actions will run the full test suite automatically on every push. Check the **Actions** tab in your repo to see your score.

---

## 📝 Part 1 — Variables & Data Types  `starter/python_basics.py` (30 pts)

Implement six functions that demonstrate your understanding of Python's built-in types, type conversion, and string formatting.

| Function | Points |
|----------|--------|
| `create_student_info` | 5 |
| `convert_temperature` | 5 |
| `classify_number` | 5 |
| `format_greeting` | 5 |
| `calculate_bmi` | 5 |
| `safe_divide` | 5 |

---

## 📝 Part 2 — Data Structures  `starter/data_structures.py` (40 pts)

Implement eight functions covering Python's core data structures.

| Function | Points |
|----------|--------|
| `get_unique_sorted` | 5 |
| `merge_and_sort` | 5 |
| `count_word_frequency` | 5 |
| `get_top_n` | 5 |
| `flatten_one_level` | 5 |
| `invert_dictionary` | 5 |
| `common_elements` | 5 |
| `group_by_first_letter` | 5 |

---

## 📝 Part 3 — Control Flow  `starter/control_flow.py` (30 pts)

Implement six functions that use `if`, `for`, `while`, and list comprehensions.

| Function | Points |
|----------|--------|
| `grade_calculator` | 5 |
| `fizzbuzz` | 5 |
| `sum_of_evens` | 5 |
| `is_prime` | 5 |
| `find_primes` | 5 |
| `collatz_length` | 5 |

---

## 🔁 GitHub Workflow Requirements

Your submission **must** show evidence of incremental commits. We expect to see at least **three commits** — one per part. Submissions with only a single commit lose 10 pts.

```
Good commit history example:
  feat: complete Part 1 – variables and data types
  feat: complete Part 2 – data structures
  feat: complete Part 3 – control flow
```

---

## ❓ Getting Help

* Post in the course discussion forum with the label `assignment-1`.
* Tag your instructor if the GitHub Actions check fails for a reason you cannot debug.
* **Do not share your solution code publicly** — that violates the honour policy.

---

## 📊 Grading Rubric

| Category | Weight |
|----------|--------|
| Autograded tests pass | 90 % |
| Commit history (≥ 3 meaningful commits) | 10 % |

The autograder runs `pytest tests/ --tb=short` and reports per-test pass/fail. Partial credit is awarded per function.

---

*Good luck and have fun! 🐍*
