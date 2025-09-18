#!/usr/bin/env python3
"""
Simple test runner for Task 1 tests.
Run this script to execute all test cases for the bump_version function.
"""

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

def run_tests():
    """Run all test cases and display results."""
    print("=" * 60)
    print("RUNNING TEST CASES FOR TASK 1 - BUMP VERSION FUNCTION")
    print("=" * 60)
    
    # Load and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_task1')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED! 🎉")
        print(f"Total tests run: {result.testsRun}")
        print("All test cases are working correctly.")
    else:
        print("❌ SOME TESTS FAILED")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
