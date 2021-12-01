from python_testing.student.project.student import Student

import unittest

class StudentTests(unittest.TestCase):

    def setUp(self):

        self.s = Student('Harry')

    def test_init_without_course(self):

        s = Student('Harry')
        self.assertEqual("Harry", s.name)
        self.assertEqual({}, s.courses)

    def test_init_with_course(self):

        s = Student('Harry', {"Python": ['note1']})
        self.assertEqual("Harry", s.name)
        self.assertEqual({"Python": ['note1']}, s.courses)

    def test_init_with_none_course(self):

        s = Student('Harry', None)
        self.assertEqual("Harry", s.name)
        self.assertEqual({}, s.courses)

    def test_enroll_duplicate_course(self):

        self.s.courses = {'Python': ['note1']}
        res = self.s.enroll('Python', ['note2'])
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(['note1', 'note2'], self.s.courses["Python"])

    def test_enroll_new_course_with_notes(self):

        res = self.s.enroll('Python', ['note1'])
        self.assertEqual("Course and course notes have been added.", res)
        self.assertEqual(self.s.courses['Python'], ['note1'])

    def test_enroll_new_course_without_adding_notes(self):

        res = self.s.enroll('Python', ['note1'], 'no')
        self.assertEqual("Course has been added.", res)
        self.assertEqual(self.s.courses['Python'], [])

    def test_enroll_new_course_with_adding_notes(self):

        res = self.s.enroll('Python', ['note1', 'note2'], 'Y')
        self.assertEqual("Course and course notes have been added.", res)
        self.assertEqual(self.s.courses['Python'], ['note1', 'note2'])

    def test_enroll_in_existing_course_with_adding_notes(self):

        self.s.enroll('Python', ['note1', 'note2'], 'Y')
        res = self.s.enroll('Python', ['note3'], 'Y')
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(self.s.courses['Python'], ['note1', 'note2', 'note3'])

    def test_add_notes(self):

        self.s.courses = {'Python': []}
        res = self.s.add_notes('Python', 'note1')
        self.assertEqual('Notes have been updated', res)
        self.assertEqual(['note1'], self.s.courses['Python'])

    def test_add_notes_exception(self):

        with self.assertRaises(Exception) as e:
            self.s.add_notes("Java", "note_fail")
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))
        self.assertEqual({}, self.s.courses)

    def test_leave_course(self):

        self.s.courses = {'Python': []}
        res = self.s.leave_course('Python')
        self.assertEqual("Course has been removed", res)
        self.assertEqual({}, self.s.courses)

    def test_leave_course_exception(self):

        with self.assertRaises(Exception) as e:
            self.s.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))

if __name__ == "__main__":
    unittest.main()