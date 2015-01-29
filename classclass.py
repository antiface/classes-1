class Course:
	def __init__(self, capacity, title, instructor=None):
		self.title = ""
		self.schedule = Schedule()
		self.students = []
		self.capacity = capacity
		self.instructor = instructor

	def add_student(self, student):
		if self.students.length() == self.capacity:
			self.students.append(student)
			return True
		## check if schedule permits
		print "Class full. Cannot add more students."
		return False

	def remove_student(self, student):
		if self.students.length() > 0 and student in self.students:
			self.students.remove(student)
			## clear schedule of student for that class
			return True
		print "Error: class empty or student not in class." 
		return False

	# def list_students(self):
	#   for student in self.students:
	#       print student

	def available_spots(self):
		return self.capacity - self.students.length 

class Student:
	def __init__(self, name, courses=None):
		self.name = name
		self.schedule = Schedule()
		self.courses = courses 

	def get_courses(self):
		for day, time in self.schedule:
			print day, time


class Schedule:
	def __init__(self, schedule_dict=None):
		if schedule_dict is None:
			schedule_dict = {"M": [],
							 "T": [],
							 "W": [],
							 "Th": [],
							 "F": [],
							 "Sat": [],
							 "Sun": []}

		self.schedule_dict = schedule_dict

	def add_schedule(self, schedule):
		'''
			Add second schedule to the first schedule if no conflict
			Return true if s1 and s2 contain a conflict

		'''
		for day_one in self.schedule_dict:
			for day_two in schedule.schedule_dict:
				# print day_one
				# print day_two
				if day_one == day_two:
					day1 = self.schedule_dict[day_one]
					day2 = schedule.schedule_dict[day_two]

					# print day1
					# print day2

					for course1 in day1:
						for course2 in day2:

							late_course = course1 if course1[1] > course2[1] else course2
							early_course = course1 if course1[0] < course2[0] else course2

							if early_course == late_course or early_course[1] > late_course[0]:
								return True

		for day_one in self.schedule_dict:
			for day_two in schedule.schedule_dict:

				if day_one == day_two:
					self.schedule_dict[day_one].append(schedule.schedule_dict[day_two])
		# print self.schedule_dict
		return False


	def remove_schedule(self, schedule):
		for day in self.schedule_dict:
			for course in schedule.schedule_dict[day]:
				# Going to get every course in day we're evaluating
				if course in self.schedule_dict[day]:
					self.schedule_dict[day].remove(course)
		# return self.schedule_dict

# student_sched = Schedule()
# course_sched = Schedule()

# student_sched.add_schedule(course_sched)

# schedule_dict1 = {"M": [(8, 10), (11, 12), (2, 5)],
# 				 "T": [],
# 				 "W": [],
# 				 "Th": [],
# 				 "F": [],
# 				 "Sat": [],
# 				 "Sun": []
# 				}

# schedule_dict2 = {"M": [(8, 10)],
# 				 "T": [],
# 				 "W": [],
# 				 "Th": [],
# 				 "F": [],
# 				 "Sat": [],
# 				 "Sun": []
# 				}

# schedule_dict1 = Schedule(schedule_dict1)
# schedule_dict2 = Schedule(schedule_dict2)

# schedule_dict1.remove_schedule(schedule_dict2)

# print schedule_dict1


class CourseCatalogue:
	def __init__(self, courses=[]):
		self.courses = courses

	def add_course(self, course):
		self.courses.append(course)
		return self.courses


	def remove_course(self, course):
		if course in self.courses:
			self.courses.remove(course)
			return self.courses
		else:
			# course does not exist
			return False


