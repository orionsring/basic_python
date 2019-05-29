import xml.etree.ElementTree as ET
tree = ET.parse('courses.xml')
course_els = tree.findall('course')
course_names = [
    course.fine('title').text for course in course_els]
ratings = [
    course.find('rating').attrib['stars'] for course in course_els]

