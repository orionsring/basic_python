import xml.etree.ElementTree as ET
course_data = ET.parse('courses.xml')
root = course_data.getroot()
root.tag
#'courses'

all_courses=root.findall('course')
len(all_courses)
#10
all_ratings= [course.find('rating') for course in all_courses]
all_ratings = root.findall('course/rating')
votes=[rating.attrib['votes'] for rating in all_ratings]
total=sum(votes)
#TypeError