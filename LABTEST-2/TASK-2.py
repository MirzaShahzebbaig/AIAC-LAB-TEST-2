
def normalize(scores):
    """Normalizes a list of numeric scores to the [0, 1] range.

    This function rescales the input list so that the minimum value becomes 0 and the maximum becomes 1.
    If all values are equal, returns a list of zeros of the same length.
    If the input list is empty, returns an empty list.

    Args:
        scores (list of float or int): The list of numeric scores to normalize.

    Returns:
        list of float: The normalized scores in the [0, 1] range.

    Examples:
        >>> normalize([10, 20, 30])
        [0.0, 0.5, 1.0]

        >>> normalize([5, 5, 5])
        [0.0, 0.0, 0.0]

        >>> normalize([])
        []

        >>> normalize([3])
        [0.0]
    """
    if not scores:
        return []
    m = max(scores)
    n = min(scores)
    if m == n:
        return [0.0] * len(scores)
    return [(x - n) / (m - n) for x in scores]

if __name__ == "__main__":
    # Read values from the console, separated by spaces or commas
    input_str = input("Enter numbers separated by spaces or commas: ").strip()
    if ',' in input_str:
        items = [s.strip() for s in input_str.split(',') if s.strip()]
    else:
        items = [s.strip() for s in input_str.split() if s.strip()]
    # Try to convert to float, skip invalid entries
    scores = []
    for item in items:
        try:
            scores.append(float(item))
        except ValueError:
            pass
    print(normalize(scores))

import unittest

class TestNormalize(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(normalize([10, 20, 30]), [0.0, 0.5, 1.0])
        self.assertEqual(normalize([1, 2, 3, 4]), [0.0, 0.3333333333333333, 0.6666666666666666, 1.0])

    def test_empty_list(self):
        self.assertEqual(normalize([]), [])

    def test_all_equal(self):
        self.assertEqual(normalize([5, 5, 5]), [0.0, 0.0, 0.0])
        self.assertEqual(normalize([0, 0]), [0.0, 0.0])
        self.assertEqual(normalize([42]), [0.0])

    def test_negative_numbers(self):
        self.assertEqual(normalize([-1, 0, 1]), [0.0, 0.5, 1.0])
        self.assertEqual(normalize([-5, -5, -5]), [0.0, 0.0, 0.0])

    def test_floats(self):
        result = normalize([1.5, 2.5, 3.5])
        expected = [0.0, 0.5, 1.0]
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e)

if __name__ == "__main__":
    unittest.main()
