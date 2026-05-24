"""
Root conftest.py
================
Ensures the project root is on sys.path so that
`from starter.xxx import yyy` works from any test.
"""
import sys
import os

# Add the repository root to sys.path
sys.path.insert(0, os.path.dirname(__file__))
