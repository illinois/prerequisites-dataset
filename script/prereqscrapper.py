import pandas as pd
import csv
from uiuccourses import *

# object to store a course and its prereqs
class Course:
    def __init__(self, title):
        self.title = title
        self.prereqs = []


# load in csv from https://github.com/illinois/courses-dataset
courses = pd.read_csv("data/2019-fa.csv", header=0)

# create dict to store courses & loop through courses
course_dict = dict()
rows = len(courses.index)
for x in range(0, rows):
    # make object for course, setting title to course code
    c = Course(courses.loc[x, 'Subject'] + " " + str(courses.loc[x, 'Number']))

    # find "Prerequisite" in the description, and isolate that sentence's string.
    descrip = courses.loc[x, 'Description']
    if type(descrip) is str: # do not parse empty / non-string rows
        if "Prerequisite" in descrip:
            # get the string starting from "Prerequisite" and ending in "."
            starts = descrip.find("Prerequisite")
            ends = descrip.find(".", starts)
            prtext = descrip[starts:ends]

            # get list of prereqs, set that to the object
            c.prereqs.extend(containsCourseCodes(prtext))

    # add course to dictionary
    course_dict[c.title] = c

# search descriptions for "See [Course Code]," give course prereq of coresponding course
# (most descriptions that tell you to see a different course don't include their own prereq data)
for x in range(0, rows):
    descrip = courses.loc[x, 'Description']

    if (type(descrip) is str):
        code = seeCode(descrip)
        if code and code in course_dict: # since the university doesn't always update their records,
        # sometimes it will tell us to see a course that doesn't exist: (oops!) we're going to give up on finding the prereqs then
            course_dict[courses.loc[x, 'Subject'] + " " + str(courses.loc[x, 'Number'])].prereqs.extend(course_dict[code].prereqs)

# save course prereqs into new csv
w = csv.writer(open("uiuc-prerequisites.csv", "w"))
w.writerow(["Course", "PrerequisiteNumber", "Prerequisites"])
for title in sorted(course_dict):
    prereq_number = len(course_dict[title].prereqs)
    course_dict[title].prereqs.insert(0, title)
    course_dict[title].prereqs.insert(1, prereq_number)
    w.writerow(course_dict[title].prereqs)
