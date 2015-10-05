import unittest
import studentpath
from collections import OrderedDict
 
class TestPaths(unittest.TestCase):
 
    def setUp(self):
        self.domainOrderContentExpected = [['K', 'RF', 'RL', 'RI'], ['1', 'RF', 'RL', 'RI'], ['2', 'RF', 'RI', 'RL', 'L'], ['3', 'RF', 'RL', 'RI', 'L'], ['4', 'RI', 'RL', 'L'], ['5', 'RI', 'RL', 'L'], ['6', 'RI', 'RL']]
        self.studentTestContent = [{'RL': '3', 'Student Name': 'Albin Stanton', 'RF': '2', 'L': '3', 'RI': 'K'}, {'RL': '1', 'Student Name': 'Erik Purdy', 'RF': '3', 'L': '1', 'RI': '1'}, {'RL': 'K', 'Student Name': 'Aimee Cole', 'RF': 'K', 'L': '2', 'RI': '1'}, {'RL': '4', 'Student Name': 'Frederik Schulist', 'RF': '2', 'L': '4', 'RI': '4'}, {'RL': '3', 'Student Name': 'Addie Green', 'RF': '2', 'L': '1', 'RI': 'K'}, {'RL': '2', 'Student Name': 'Missouri Auer', 'RF': '4', 'L': '1', 'RI': '1'}, {'RL': '5', 'Student Name': 'Christopher Hayes', 'RF': '5', 'L': '2', 'RI': 'K'}, {'RL': 'K', 'Student Name': 'Enos Jacobi', 'RF': 'K', 'L': '5', 'RI': '4'}, {'RL': '5', 'Student Name': 'Conrad Nitzsche', 'RF': '1', 'L': '3', 'RI': 'K'}, {'RL': '3', 'Student Name': 'Jazlyn Wisoky', 'RF': '4', 'L': '3', 'RI': '5'}, {'RL': '2', 'Student Name': 'Kelley Emard', 'RF': 'K', 'L': '4', 'RI': 'K'}, {'RL': '4', 'Student Name': 'Dell Kozey', 'RF': 'K', 'L': '2', 'RI': '3'}, {'RL': '4', 'Student Name': 'Kraig Goldner', 'RF': '5', 'L': '3', 'RI': '2'}, {'RL': '5', 'Student Name': 'Stephon Ondricka', 'RF': '5', 'L': 'K', 'RI': '3'}, {'RL': '1', 'Student Name': 'Tracey Lind', 'RF': 'K', 'L': '1', 'RI': '3'}, {'RL': '3', 'Student Name': 'Elissa Schinner', 'RF': '5', 'L': '4', 'RI': '1'}, {'RL': '3', 'Student Name': 'Orpha Bartoletti', 'RF': '1', 'L': 'K', 'RI': '2'}, {'RL': '1', 'Student Name': 'Timmothy Torphy', 'RF': 'K', 'L': '1', 'RI': 'K'}, {'RL': '3', 'Student Name': 'Maia Torphy', 'RF': 'K', 'L': '1', 'RI': '2'}, {'RL': '5', 'Student Name': 'Danyka Pfeffer', 'RF': '5', 'L': '2', 'RI': '5'}, {'RL': 'K', 'Student Name': "Leo O'Connell", 'RF': '3', 'L': '1', 'RI': 'K'}, {'RL': '3', 'Student Name': 'Scotty Kovacek', 'RF': 'K', 'L': '1', 'RI': '3'}, {'RL': '4', 'Student Name': 'Cameron Prohaska', 'RF': '2', 'L': '4', 'RI': '2'}, {'RL': '4', 'Student Name': 'Angus Torp', 'RF': '2', 'L': '1', 'RI': '5'}, {'RL': '1', 'Student Name': 'Douglas Feil', 'RF': '1', 'L': 'K', 'RI': '1'}, {'RL': 'K', 'Student Name': 'Maxime Runte', 'RF': '2', 'L': 'K', 'RI': '4'}, {'RL': 'K', 'Student Name': 'Mortimer Denesik', 'RF': 'K', 'L': '3', 'RI': '2'}, {'RL': '5', 'Student Name': 'Bennett Muller', 'RF': '5', 'L': '1', 'RI': '5'}, {'RL': '2', 'Student Name': 'Ayana Runolfsson', 'RF': 'K', 'L': '2', 'RI': '5'}, {'RL': '3', 'Student Name': 'Angelina Runolfsson', 'RF': 'K', 'L': '1', 'RI': '1'}]
        self.expectedStudentPath = OrderedDict([((0, 'RF'), ''), ((0, 'RL'), ''), ((0, 'RI'), ''), ((1, 'RF'), ''), ((1, 'RL'), ''), ((1, 'RI'), ''), ((2, 'RF'), ''), ((2, 'RI'), ''), ((2, 'RL'), ''), ((2, 'L'), ''), ((3, 'RF'), ''), ((3, 'RL'), ''), ((3, 'RI'), ''), ((3, 'L'), ''), ((4, 'RI'), ''), ((4, 'RL'), ''), ((4, 'L'), ''), ((5, 'RI'), ''), ((5, 'RL'), ''), ((5, 'L'), ''), ((6, 'RI'), ''), ((6, 'RL'), '')])
 
    def test_junk_readFile(self):
        self.assertRaises(ValueError, studentpath.readFiles, "sdfsdf","sdfdsf")

    def test_valid_readFile(self):
	domainOrderContent, studentTestContent = studentpath.readFiles("./data/domain_order.csv", "./data/student_tests.csv")
	self.assertEqual( (domainOrderContent, studentTestContent), (self.domainOrderContentExpected,self.studentTestContent))
 
    def test_getClasspath(self):
	gradeToLevels,levelToGrades,classPath = studentpath.getClassPath(self.domainOrderContentExpected)
        self.assertEqual( classPath, self.expectedStudentPath)

    def test_matchesExample(self):
	import sys
	from StringIO import StringIO
	stdout = sys.stdout
	out = StringIO()
	with open('./data/sample_solution.csv') as f:
    		expected = f.readlines()
	try:
		sys.stdout = out
		gradeToLevels,levelToGrades,classPath = studentpath.getClassPath(self.domainOrderContentExpected)
		studentpath.getStudentPath(gradeToLevels,levelToGrades,classPath,self.studentTestContent)
		output = out.getvalue()
		
		self.assertEqual(output,''.join(expected))
	finally:
		sys.stdout = stdout
		
 
if __name__ == '__main__':
    unittest.main()
