import unittest
import pandas as pd
import os
import tempfile
from combine_excel import read_excel_files, combine_data_frames

class TestCombineExcelFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        # Create mock Excel files in the temporary directory
        self.file_paths = []
        for i in range(2):
            file_path = os.path.join(self.test_dir.name, f'test{i}.xlsx')
            df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
            df.to_excel(file_path, index=False)
            self.file_paths.append(file_path)

    def tearDown(self):
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_read_excel_files(self):
        # Test reading files from the temporary directory
        data_frames = read_excel_files(self.test_dir.name)
        self.assertEqual(len(data_frames), 2)

    def test_combine_data_frames(self):
        # Test combining DataFrames
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
        combined_df = combine_data_frames([df1, df2])
        self.assertEqual(combined_df.shape, (4, 2))

if __name__ == "__main__":
    unittest.main()
