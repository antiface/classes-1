
def test_schedules(schedule1, schedule2):
	'''
		Add second schedule to the first schedule if no conflict
		Return true if s1 and s2 contain a conflict

	'''
	for day_one in schedule1:
		for day_two in schedule2:
			# print day_one
			# print day_two
			if day_one == day_two:
				day1 = schedule1[day_one]
				day2 = schedule2[day_two]

				# print day1
				# print day2

				for course1 in day1:
					for course2 in day2:

						late_course = course1 if course1[1] > course2[1] else course2
						early_course = course1 if course1[0] < course2[0] else course2

						if early_course == late_course or early_course[1] > late_course[0]:
							return True

	for day_one in schedule1:
		for day_two in schedule2:

			if day_one == day_two:
				schedule1[day_one].append(schedule2[day_two])
	print schedule1
	return False

schedule_dict1 = {"M": [(8, 10), (11, 12), (2, 5)],
				 "T": [],
				 "W": [],
				 "Th": [],
				 "F": [],
				 "Sat": [],
				 "Sun": []
				}

schedule_dict2 = {"M": [(9, 11), (18,20), (21, 23)],
				 "T": [],
				 "W": [],
				 "Th": [],
				 "F": [],
				 "Sat": [(2, 3)],
				 "Sun": []
				}

schedule_dict3 = {"M": [(6,8), (3,4)],
				 "T": [],
				 "W": [],
				 "Th": [],
				 "F": [],
				 "Sat": [(4, 6)],
				 "Sun": []
				}

schedule_dict4 = {"M": [(7,9)],
				 "T": [],
				 "W": [],
				 "Th": [],
				 "F": [],
				 "Sat": [],
				 "Sun": []
				}

schedule_dict5 = {"M": [(7,8)],
				 "T": [],
				 "W": [],
				 "Th": [],
				 "F": [],
				 "Sat": [],
				 "Sun": []
				}

print test_schedules(schedule_dict1, schedule_dict2) # True
print test_schedules(schedule_dict2, schedule_dict3) # False
print test_schedules(schedule_dict1, schedule_dict3) # True
print test_schedules(schedule_dict4, schedule_dict1) # True
print test_schedules(schedule_dict5, schedule_dict1) # False
print test_schedules(schedule_dict5, schedule_dict4) # True
print test_schedules(schedule_dict5, schedule_dict4) # True





