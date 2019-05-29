import csv
ps_data =  open('ps_data.csv', 'r')
dr = csv.DictReader(ps_data)
import json
print(json.dumps(rows))

for row in rows:
    first_name = row.pop('first_name', None)
    last_name = row.pop('last_name', None)
    row['author'] = {'first_name': first_name, 'last_name': last_name}

for row in rows:
    author = row.pop('author', None)
    row['authors'] = [author]

rows[2]['authors'].append({'first_name': 'Joe', 'last_name': 'Eames'})
print(json.dumps(rows))

courses = json.loads(json.dumps(rows))

courses

total_authors = sum([len(course['authors']) for course in courses])
total_authors
# 6

avg_votes = sum([int(course[;votes']) for course in courses]\)/ len(courses
avg_votes#846.4

