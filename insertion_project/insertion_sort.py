import unittest

# Create the insertion sorting function.
def insertion_sort(A, n):
    # 'A' is the array of values to be sorted, 'n' being the numbers of values to sort.
    # Traverse through 1 to n.
    for i in range(1, n):
        # ^ i = range of number values from 1 to n, n being the highest possible number in the array.
        # Defining key
        key = A[i]
        # Move elements of n[0 to i-1] that are greater than key to one position ahead of current position.
        j = i - 1
        # Looping for sorting the number values until they're in the correct position.
        while j >= 0 and A[j] > key:
            print('Key:', key, 'Array:', A, 'Pre Pos. checker:', j)
            A[j + 1] = A[j]
            j = j - 1
            print('Pos.Checker:', j, """
            """)
        # Place the key at it's correct position.
        A[j + 1] = key

class TestInsertionSort(unittest.TestCase):

    # Test insertion sorting, basic numbering.
    def test_insertion_sort_basic(self):
        # Define the sequence.
        A = [6, 5, 2, 1, 3, 4]
        # Input the sequence into the sorting mechanism.
        insertion_sort(A, len(A))
        # Assert if the sequence is in numerical order.
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])

    # Test insertion sorting, exercise on pg. 24.
    def test_insertion_sort_exercise(self):
        # Define the sequence.
        A = [31, 41, 59, 26, 41, 58]
        # Input the sequence into the sorting mechanism.
        insertion_sort(A, len(A))
        # Assert if the sequence is in numerical order.
        self.assertEqual(A, [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    unittest.main()