import unittest


def generate_paths():
    return [(0, x, y) for x in range(2) for y in range(3)]


def is_valid_path(path):
    for idx, i in enumerate(path):
        if idx + 1 == len(path):
            break
        if all([(path[idx + 1] != i),
                (path[idx + 1] != (i + 1))]):
            return False
    return True


def find_sum(arrays):
    """returns the greatest sum and the bottom number
    """
    paths = generate_paths()
    greatest_sum = 0
    sum = 0
    bottom_index = 0
    for path in paths:
        if is_valid_path(path):
            sum = arrays[0][path[0]] + arrays[1][path[1]] + arrays[2][path[2]]
        if sum > greatest_sum:
            greatest_sum = sum
            bottom_index = path[2]
    return (greatest_sum, bottom_index)


def solution():
    y = 0  # pointer to current array in arrays
    sum = 0
    arrays = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
    for i in range((len(arrays) / 3)):
        y += 3

    print sum


class Tests(unittest.TestCase):

    def test_valid_path(self):
        self.assertFalse(is_valid_path((0, 0, 2)))
        self.assertTrue(is_valid_path((0, 0, 1)))
        self.assertFalse(is_valid_path((0, 1, 0)))

    def test_find_sum(self):
        self.assertEqual(
            find_sum([
                [75],
                [95, 64],
                [17, 47, 82],
                ]),
            (221, 2))
        self.assertEqual(
            find_sum([
                [1],
                [1, 0],
                [1, 0, 0],
                ]),
            (3, 0))


if __name__ == '__main__':
    unittest.main()

# solution()
