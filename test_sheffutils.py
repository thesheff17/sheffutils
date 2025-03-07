#!/usr/bin/env python3

# standard library imports
import os
import re
import unittest
import zipfile

# 3rd party imports
import sheffutils

class TestDateFormat(unittest.TestCase):
    def test_hello_world(self):
        assert "hello world" == sheffutils.hello_world()

    def test_date_format(self):
        """Tests the format YYYY-MM-DD-HH-MM-SS-000000."""
        pattern = r"^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-\d{6}$"

        # Positive test cases
        self.assertTrue(re.match(pattern, "2025-03-02-11-01-50-000000"))

    def test_ollama_list(self):
        text1 = sheffutils.ollama_list_read(file1="test/test_ollama_list.txt")
        self.assertTrue(text1[0].name == "llama3.2:1b", msg="The ollama name did not match from the data class")
        self.assertTrue(text1[0].id == "baf6a787fdff")
        self.assertTrue(text1[0].size == '1.3 GB', msg=f"{text1[0].size}")
        self.assertTrue(text1[0].modified == "3 weeks ago", msg=f"{text1[0].modified}")

    def test_zip_files(self):
        destination = "test/my_archive.zip"
        if os.path.isfile(destination):
            os.remove(destination)
        files_to_zip = ["test/file1.txt", "test/file2.txt"]
       
        c1 = sheffutils.zip_files(files_to_zip, destination)
        self.assertTrue(c1)

        with zipfile.ZipFile(destination, 'r') as zipf:
            file_list = zipf.namelist()
        
        self.assertTrue(files_to_zip, file_list)
