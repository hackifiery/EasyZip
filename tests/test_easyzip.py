import os
import sys
import unittest
from EasyZip.easyzip import EasyZip

class TestEasyZip(unittest.TestCase):

    def setUp(self):
        # Create a temporary test directory for testing
        self.test_directory = 'test_directory'
        os.makedirs(self.test_directory, exist_ok=True)
        self.zip_filename = 'test.zip'
        self.extract_path = 'test_extracted_directory'

    def tearDown(self):
        # Clean up the temporary test directory and files
        if os.path.exists(self.zip_filename):
            os.remove(self.zip_filename)
        if os.path.exists(self.extract_path):
            for root, _, files in os.walk(self.extract_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
            os.rmdir(self.extract_path)
        if os.path.exists(self.test_directory):
            os.rmdir(self.test_directory)

    def test_create_and_extract_zip(self):
        # Test creating a zip file and extracting its contents
        with EasyZip(self.zip_filename) as ez:
            ez.add_file('file1.txt')
            ez.add_directory(self.test_directory)

        with EasyZip(self.zip_filename) as ez:
            ez.extract_to(self.extract_path)

        # Check if the extracted directory contains the same files as the test directory
        test_files = set(os.listdir(self.test_directory))
        extracted_files = set(os.listdir(self.extract_path))
        self.assertEqual(test_files, extracted_files)

if __name__ == '__main__':
    unittest.main()
