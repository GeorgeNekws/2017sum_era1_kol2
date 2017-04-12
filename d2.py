
def main():
	
	python_dict = { "Geo" :[7.0,8.0,10.0] , 'Nick':[5.0,9.0] }
	java_dict = { "Tom" :[9.0,8.0,5.0] , 'Nox':[4.0,8.0,5.0,9.0], 'Lena':[2.0,9.0] }
	physics_dict = { "Tom" :[4.0,8.0,4.0] , 'Geo':[8.0,9.0], 'Lena':[9.0,9.0] }
	
	dict_course = { 'Python' : python_dict , 'Java': java_dict, 'Physics': physics_dict  }
	
	button = 9
	while button != 0:
		
		lesson_exists = 0
		found = 0 
		attend = 0
		avg = 0
		add = 0
		num_of_grades = 0
		
		print 'choose 1 to take AVG of a student in a course'
		print 'choose 2 to take AVG of a student in every course'
		print 'press zero (0) to exit'
		button = int(raw_input('Choose one of the options above : '))
		
		if button == 1:
			
			name = raw_input('Give the student name : ')
			course = raw_input('Give the course name : ')
			
			for lesson in dict_course:								# for each lesson in dictionary
				if lesson == course:								# we check if the "required lesson exists"
					lesson_exists = 1
					print "The course you entered exists\n"
					students = dict_course.get(lesson)				# i take the dictionary of the students attend this course
					
					for student in students: 
						if student == name:							# i check if the "required student" attend the "required course"
							found = 1
							print "student attend this course\n"
							grades = students.get(student)			# i take the grades of the student 
							#print grades
							length = len(grades)
							
							for i in range(0,length):				# loop over the grades list
								add = add + grades[i]
								
							avg = add / (i+1)						# i calculate the avg
							print avg
							break
					if found == 0:
						print 'This student does NOT attend this course\n'
			if lesson_exists == 0:
				print "The course you entered does NOT exists\n"
	
			
		elif button == 2:
			
			name = raw_input('Give the student name : ')
			
			for lesson in dict_course:							# for each lesson in dictionary
				students = dict_course.get(lesson)				# students var : has a dictionary with student names as key 
				
				for student in students: 						# for each student that attends this lesson 
					if student == name:							#i check if the "required student" attends the lesson
						print "student attend this course"
						attend = attend + 1
						grades = students.get(student)			
						#print grades
						length = len(grades) 
							
						for i in range(0,length):				# calculation of sum of grades for each lesson
							add = add + grades[i]		
							
						num_of_grades = num_of_grades + i + 1	# number of grades + 1 , because counter i ,starts from 0

						
	
			avg = add / (num_of_grades)							# calculation of avg of all courses
			print 'Avg is : '
			print avg

				
if __name__ == "__main__":
	main()
			
