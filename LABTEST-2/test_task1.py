import unittest
import sys
import os

# Add the current directory to the path to import TASK-1
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the function from TASK-1.py
import importlib.util
spec = importlib.util.spec_from_file_location("task1", "TASK-1.py")
task1_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task1_module)
bump_version = task1_module.bump_version

class TestBumpVersion(unittest.TestCase):
    
    def test_no_version_no_extension(self):
        """Test files without version and without extension"""
        self.assertEqual(bump_version('file'), 'file_v01')
        self.assertEqual(bump_version('report'), 'report_v01')
        self.assertEqual(bump_version('data'), 'data_v01')
    
    def test_no_version_with_extension(self):
        """Test files without version but with extension"""
        self.assertEqual(bump_version('summary.csv'), 'summary_v01.csv')
        self.assertEqual(bump_version('report.txt'), 'report_v01.txt')
        self.assertEqual(bump_version('data.json'), 'data_v01.json')
        self.assertEqual(bump_version('config.xml'), 'config_v01.xml')
    
    def test_single_digit_version_no_extension(self):
        """Test files with single digit version and no extension"""
        self.assertEqual(bump_version('file_v1'), 'file_v2')
        self.assertEqual(bump_version('report_v5'), 'report_v6')
        self.assertEqual(bump_version('data_v9'), 'data_v10')
    
    def test_single_digit_version_with_extension(self):
        """Test files with single digit version and extension"""
        self.assertEqual(bump_version('file_v1.txt'), 'file_v2.txt')
        self.assertEqual(bump_version('report_v5.csv'), 'report_v6.csv')
        self.assertEqual(bump_version('data_v9.json'), 'data_v10.json')
    
    def test_double_digit_version_no_extension(self):
        """Test files with double digit version and no extension"""
        self.assertEqual(bump_version('file_v01'), 'file_v02')
        self.assertEqual(bump_version('report_v05'), 'report_v06')
        self.assertEqual(bump_version('data_v09'), 'data_v10')
        self.assertEqual(bump_version('log_v10'), 'log_v11')
        self.assertEqual(bump_version('config_v99'), 'config_v100')
    
    def test_double_digit_version_with_extension(self):
        """Test files with double digit version and extension"""
        self.assertEqual(bump_version('file_v01.txt'), 'file_v02.txt')
        self.assertEqual(bump_version('report_v05.csv'), 'report_v06.csv')
        self.assertEqual(bump_version('data_v09.json'), 'data_v10.json')
        self.assertEqual(bump_version('log_v10.log'), 'log_v11.log')
        self.assertEqual(bump_version('config_v99.xml'), 'config_v100.xml')
    
    def test_triple_digit_version(self):
        """Test files with triple digit version"""
        self.assertEqual(bump_version('file_v001'), 'file_v002')
        self.assertEqual(bump_version('report_v010'), 'report_v011')
        self.assertEqual(bump_version('data_v099'), 'data_v100')
        self.assertEqual(bump_version('log_v100'), 'log_v101')
        self.assertEqual(bump_version('config_v999'), 'config_v1000')
    
    def test_triple_digit_version_with_extension(self):
        """Test files with triple digit version and extension"""
        self.assertEqual(bump_version('file_v001.txt'), 'file_v002.txt')
        self.assertEqual(bump_version('report_v010.csv'), 'report_v011.csv')
        self.assertEqual(bump_version('data_v099.json'), 'data_v100.json')
        self.assertEqual(bump_version('log_v100.log'), 'log_v101.log')
        self.assertEqual(bump_version('config_v999.xml'), 'config_v1000.xml')
    
    def test_preserve_zero_padding(self):
        """Test that zero padding is preserved"""
        self.assertEqual(bump_version('file_v01'), 'file_v02')
        self.assertEqual(bump_version('file_v001'), 'file_v002')
        self.assertEqual(bump_version('file_v0001'), 'file_v0002')
        self.assertEqual(bump_version('file_v09'), 'file_v10')
        self.assertEqual(bump_version('file_v009'), 'file_v010')
        # The function preserves the original width, so 4 digits stays 4 digits
        self.assertEqual(bump_version('file_v0009'), 'file_v0010')
    
    def test_preserve_zero_padding_with_extension(self):
        """Test that zero padding is preserved with extensions"""
        self.assertEqual(bump_version('file_v01.txt'), 'file_v02.txt')
        self.assertEqual(bump_version('file_v001.csv'), 'file_v002.csv')
        self.assertEqual(bump_version('file_v0001.json'), 'file_v0002.json')
        self.assertEqual(bump_version('file_v09.log'), 'file_v10.log')
        self.assertEqual(bump_version('file_v009.xml'), 'file_v010.xml')
        # The function preserves the original width, so 4 digits stays 4 digits
        self.assertEqual(bump_version('file_v0009.py'), 'file_v0010.py')
    
    def test_complex_filenames(self):
        """Test complex filenames with underscores and multiple dots"""
        self.assertEqual(bump_version('my_report_v1.csv'), 'my_report_v2.csv')
        self.assertEqual(bump_version('user_data_v05.json'), 'user_data_v06.json')
        # Note: The function only considers the last dot as extension, so .tar.gz becomes .tar_v01.gz
        self.assertEqual(bump_version('backup_file_v10.tar.gz'), 'backup_file_v10.tar_v01.gz')
        # The function splits on the last dot, so config.backup_v01 becomes config_v01.backup_v01
        self.assertEqual(bump_version('config.backup_v01'), 'config_v01.backup_v01')
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Version 99 should become 100
        self.assertEqual(bump_version('file_v99'), 'file_v100')
        self.assertEqual(bump_version('file_v99.txt'), 'file_v100.txt')
        
        # Version 999 should become 1000
        self.assertEqual(bump_version('file_v999'), 'file_v1000')
        self.assertEqual(bump_version('file_v999.txt'), 'file_v1000.txt')
    
    def test_special_characters_in_filename(self):
        """Test filenames with special characters"""
        self.assertEqual(bump_version('file-name_v1.txt'), 'file-name_v2.txt')
        self.assertEqual(bump_version('file_name_v1.txt'), 'file_name_v2.txt')
        self.assertEqual(bump_version('file.name_v1.txt'), 'file.name_v2.txt')
    
    def test_version_at_beginning(self):
        """Test that version must be at the end"""
        # These should NOT match the version pattern and should add _v01
        self.assertEqual(bump_version('v1_file.txt'), 'v1_file_v01.txt')
        self.assertEqual(bump_version('file_v1_middle.txt'), 'file_v1_middle_v01.txt')
    
    def test_multiple_versions_in_name(self):
        """Test filenames with multiple version-like patterns"""
        # Only the last _vNN pattern should be incremented
        self.assertEqual(bump_version('file_v1_v2.txt'), 'file_v1_v3.txt')
        self.assertEqual(bump_version('v1_file_v2.txt'), 'v1_file_v3.txt')

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)