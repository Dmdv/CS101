__author__ = 'dmitrijdackov'

#Dictionaries of Dictionaries (of Dictionaries)

#The next several questions concern the data structure below for keeping
#track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                 }
}


#For the following questions, you will find the
#        for <key> in <dictionary>:
#                   <block>
#construct useful.  This loops through the key values in the Dictionary.  For
#example, this procedure returns a list of all the courses offered in the given
#hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

#Define a procedure, is_offered(courses, course, hexamester), that returns True
#if the input course is offered in the input hexamester, and returns False
#otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012') => True
#print is_offered(courses, 'cs003', 'apr2012') => False

#(Note: it is okay if your procedure produces an error if the input hexamester is not included in courses.
#For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)

def is_offered(courses, course, hexamester):
    """
    Checks if the course is offered
    """
    if hexamester in courses:
        test = courses[hexamester]
        if course in test:
            return True
    return False

def when_offered(courses,course):
    """
    When course is offered
    """
    res = []
    for data in courses:
        lst = courses_offered(courses, data)
        if course in lst:
            res.append(data)
    return res

def involved(courses, person):
    """
    Courses that a person invlved in
    """
    out = {}
    for data, course in courses.items():
        arr = []
        for cname, prep in course.items():
            for pers, val in prep.items():
                if val == person:
                    arr.append(cname)
        if len(arr):
            out[data] = arr
    return out

print (involved(courses, 'Dave'))

print (when_offered (courses, 'cs101')) # => ['apr2012', 'feb2012']
print (when_offered(courses, 'bio893')) #=> []

print (is_offered(courses, 'cs101', 'apr2012'))
print (is_offered(courses, 'cs003', 'apr2012'))

