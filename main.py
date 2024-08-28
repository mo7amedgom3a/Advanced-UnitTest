#!/usr/bin/env python3
import unittest

# Discover and run all test cases in the 'tests' directory
def run_tests():
    test_loader = unittest.TestLoader() # Create a test loader 
    test_suite = test_loader.discover('test') # Discover and load all test cases in the 'test' directory
    
    test_runner = unittest.TextTestRunner() # Create a test runner
    test_runner.run(test_suite) # Run the test suite

if __name__ == '__main__':
    run_tests()
