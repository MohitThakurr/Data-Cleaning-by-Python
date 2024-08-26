import unittest
import pandas as pd
from scripts.data_cleaning import DataCleaner
#Testing
class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        self.cleaner = DataCleaner('data/sample_data.csv')
        self.cleaner = DataCleaner('data/sample_data.csv')

    def test_handle_missing_values(self):
        self.cleaner.handle_missing_values(strategy='mean', columns=['age'])
        self.assertFalse(self.cleaner.get_data()['age'].isnull().values.any())

    def test_remove_duplicates(self):
        initial_length = len(self.cleaner.get_data())
        self.cleaner.remove_duplicates()
        self.assertLess(len(self.cleaner.get_data()), initial_length)

    def test_add_column(self):
        self.cleaner.add_column('test_column', [1, 2, 3, 4, 5, 6, 7])
        self.assertIn('test_column', self.cleaner.get_data().columns)

    def test_transform_column(self):
        self.cleaner.transform_column('salary', lambda x: x / 1000)
        self.assertTrue((self.cleaner.get_data()['salary'] < 1000).all())

if __name__ == '__main__':
    unittest.main()
