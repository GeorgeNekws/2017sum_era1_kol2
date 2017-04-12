
def main():
	
	python_dict = { "Geo" :[7.0,8.0,10.0] , 'Nick':[9.0] }
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
		print 'choose 3 to enter a new student to a course'
		print 'choose 4 to insert a grade for a student'
		print 'choose 5 to insert data from file'
		print 'press zero (0) to exit\n'
		button = int(raw_input('Choose one of the options above : \n'))
		
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
							print 'AVG : '
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
			
		elif button == 3:
			
			new_st = raw_input( 'Enter new student to a course : ')
			course = raw_input( 'Enter the course : ')
	
			if course == 'Python':
				python_dict[new_st] = []
				print python_dict
		
			elif course == 'Java':
				java_dict[new_st] = []
				print physics_dict
		
			elif course == 'Physics':
				physics_dict[new_st] = []
				print physics_dict
			
			else:
				print "The lesson you entered does not exists"	
				
				
		elif button == 4:
			
			st = raw_input( 'Enter the student name : ')
			course = raw_input( 'Enter the course : ')
			new_grade = float(raw_input( 'Enter new grade to a course : '))
	
			if course == 'Python':
				for student in python_dict:
					if student == st:
						python_dict.get(student).append(new_grade)
						print python_dict
					else:
						print 'This student does not attend this course'
		
			elif course == 'Java':
				for student in java_dict:
					if student == st:
						java_dict.get(student).append(new_grade)
						print java_dict
					else:
						print 'This student does not attend this course'
		
			elif course == 'Physics':
				for student in physics_dict:
					if student == st:
						physics_dict.get(student).append(new_grade)
						print physics_dict
					else:
						print 'This student does not attend this course'
						
		elif button == 5:
			
			with open("file", "r") as f:
				for line in f:
					found = 0							# the student does not exist in our system
					info_list = line.split(" ")
		
					st = info_list[0]					#student name
					new_grade = float(info_list[1])
					course = info_list[2].rstrip('\n')
									
					# if the student exists in our system we just give him the new grade
					if course == 'Python':
						for student in python_dict:
							if student == st:
								found = 1
								python_dict.get(student).append(new_grade)

		
					elif course == 'Java':
						for student in java_dict:
							if student == st:
								found = 1
								java_dict.get(student).append(new_grade)

		
					elif course == 'Physics':
						for student in physics_dict:
							if student == st:
								found = 1
								physics_dict.get(student).append(new_grade)
								
					# if the student does NOT exists in our system we create him and we give him a grade in the appropriate course
					if found == 0:							
						if course == 'Python':
							python_dict[st] = [new_grade]
		
						elif course == 'Java':
							java_dict[st] = [new_grade]
		
						elif course == 'Physics':
							physics_dict[st] = [new_grade]

						else:
							print "The lesson you entered does not exists"	
		
								
		print python_dict
		print java_dict
		print physics_dict
				
if __name__ == "__main__":
	main()
			
