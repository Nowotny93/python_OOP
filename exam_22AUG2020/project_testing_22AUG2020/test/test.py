from python_oop_exams.project_testing_22AUG2020.student_report_card import StudentReportCard

import unittest

class StudentReportCardTests(unittest.TestCase):

    def setUp(self):

        self.s = StudentReportCard('Harry', 11)

    def test_init_(self):

        self.assertEqual('Harry', self.s.student_name)
        self.assertEqual(11, self.s.school_year)
        self.assertEqual({}, self.s.grades_by_subject)

    def test_if_name_is_invalid(self):

        with self.assertRaises(ValueError) as ex:
            self.s.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_if_year_is_invalid(self):

        with self.assertRaises(ValueError) as ex:
            self.s.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_if_year_is_invalid2(self):

        with self.assertRaises(ValueError) as ex:
            self.s.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_if_subject_not_in_dict(self):

        self.s.grades_by_subject = {}
        res = self.s.add_grade('Math', 4.50)
        self.assertTrue({'Math': [4.50]}, res)

    def test_if_subject_already_in_dict(self):

        self.s.grades_by_subject = {'Math': [4.50]}
        res = self.s.add_grade('Math', 5.50)
        self.assertTrue({'Math': [4.50, 5.50]}, res)

    def test_average_grade_per_subject(self):

        self.s.grades_by_subject = {'Math': [4.50, 5.50], 'History': [3.50, 4.50]}
        res = self.s.average_grade_by_subject()
        self.assertEqual("Math: 5.00\nHistory: 4.00", res)

    def test_average_all_grades(self):

        self.s.grades_by_subject = {'Math': [4.50, 5.50], 'History': [3.50, 4.50]}
        res = self.s.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.50", res)

    def test_no_grades(self):

        self.s.grades_by_subject = {}
        with self.assertRaises(ZeroDivisionError) as ex:
            self.s.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(ex.exception))

    def test_repr(self):

        actual_result = self.s.__repr__()
        expected_result = f"Name: {self.s.student_name}\n" \
                            f"Year: {self.s.school_year}\n" \
                            f"----------\n" \
                            f"{self.s.average_grade_by_subject()}\n" \
                            f"----------\n" \
                            f"{self.s.average_grade_for_all_subjects()}"
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()