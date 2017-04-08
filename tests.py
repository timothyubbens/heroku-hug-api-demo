import unittest
import sys

def run_unittests():
    ''' Execute Unit Tests '''
    tests = unittest.TestLoader().discover('tests/unit')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return result.wasSuccessful()

if __name__ == '__main__':
    unit_results = run_unittests()
    if unit_results:
        sys.exit(0)
    else:
        sys.exit(1)
