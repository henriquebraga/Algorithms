import unittest


class MatrixGradeTest(unittest.TestCase):

    def setUp(self):
        self.__students_grades = [
        ['João', 8, 7, 6]
        , ['Luiz', 7, 6, 3]
        , ['Paulo', 6, 9, 10]
        , ['Sérgio', 5, 6, 6]
           ]

    def test_matrix_names_place(self):
        """Test whether the names are at first position (index 0) for every matrix line."""
        expected_result = ['João', 'Luiz','Paulo', 'Sérgio']
        self.assertEqual(expected_result, [str(name[0]) for name in self.__students_grades])

    def test_grades_place(self):
        """Test whether the names are at first position (from index 1 and next numbrs) for every matrix line."""
        expected_result = [[8, 7, 6], [7, 6, 3], [6, 9, 10], [5, 6, 6]]
        self.assertEquals(expected_result, [n[1:] for n in self.__students_grades])

    def test_average(self):
        expected_result = [7, 5, 8, 5]
        grades = [n[1:] for n in self.__students_grades]
        averages = []
        for n in grades:
            average = 0
            for grade in n:
                average += grade
            averages.append(average // 3)
        print(averages)
        self.assertTrue(expected_result, averages)


