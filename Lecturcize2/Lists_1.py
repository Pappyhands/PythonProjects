dayCourses = ['Yoga', 'Calc 3', 'History']
eveCourses = ['Python']

allCourses = dayCourses + eveCourses

print "Day Courses: %s" % dayCourses
print "Evening Courses: %s" % eveCourses
print "All Courses: %s" % allCourses

dayCourses.insert(1, 'Philosophy')
print "Day Courses: %s" % dayCourses

del dayCourses[2]
print "Day Courses: %s" % dayCourses

eveCourses[0] = 'Introduction to Python'
print "Evening Courses: %s" % eveCourses