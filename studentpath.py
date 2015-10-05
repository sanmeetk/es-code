#!/usr/bin/env python2.7
import argparse
import csv
from collections import OrderedDict

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("domainOrder", help="path to domain order csv")
	parser.add_argument("studentTests", help="path to student tests csv")
	args = parser.parse_args()

	#read files
	try:
		domainOrderContent, studentTestContent = readFiles(args.domainOrder,args.studentTests)
	except ValueError as error:
		print error
		exit(-1)

	#dict with grade labels, order in which clases should be taken
	gradeToLevels,levelsToGrades,classPath = getClassPath(domainOrderContent)

	#remove classes lower than those taken and print first 5
	getStudentPath(gradeToLevels,levelsToGrades,classPath,studentTestContent)


def readFiles(domainOrder,studentTests):
		
	domainOrderContent = []
	studentTestContent = []
	try:
		with open(domainOrder, 'r') as domainOrderCsv:
			reader = csv.reader(domainOrderCsv)
			for row in reader:
				domainOrderContent.append(row)
	except IOError,csv.Error:
		raise ValueError("Issue reading from domain order csv")

	try:
		with open(studentTests, 'r') as studentTestsCsv:
			reader = csv.DictReader(studentTestsCsv)
			for row in reader:
				studentTestContent.append(row)
	except IOError,csv.Error:
		raise ValueError("Issue reading from student test csv")

	return (domainOrderContent,studentTestContent)

def getClassPath(domainOrderContent):
	gradeToLevels = {}
	levelToGrades = {}
	classPath = OrderedDict()
	#Preserve order but O(1) insert and remove

	count = 0
	for row in domainOrderContent:
		gradeToLevels[row[0]] = count
		levelToGrades[count] = row[0]
		for item in xrange(1,len(row)):
			classPath[(count,row[item])] = ''
		count = count + 1

	return (gradeToLevels,levelToGrades,classPath)

def getStudentPath(gradeToLevels,levelsToGrades,classPath,studentTestContent):
	for row in studentTestContent:
		out = ""
		path = OrderedDict(classPath)	
		out += row['Student Name']+","
		del row['Student Name']
		for domain in row:
			grade = gradeToLevels[row[domain]]
			for i in xrange(0,grade):
				try:
					del path[(i,domain)]
				except KeyError:
					pass
		next5 = (levelsToGrades[item[0]]+"."+item[1] for item in list(path)[:5])
		out+= ",".join(next5)
		print out
		

if __name__ == "__main__":
	main()





























