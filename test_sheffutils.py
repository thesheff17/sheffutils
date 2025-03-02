#!/usr/bin/env python3

# standard library imports
import re
import unittest

# 3rd party imports
import sheffutils

class TestDateFormat(unittest.TestCase):
    def test_hello_world(self):
        assert "hello world" == sheffutils.hello_world()

    def test_date_format(self):
        """Tests the format YYYY-MM-DD-HH-MM-SS."""
        pattern = r"^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$"

        # Positive test cases
        self.assertTrue(re.match(pattern, "2025-03-02-11-01-50"))
