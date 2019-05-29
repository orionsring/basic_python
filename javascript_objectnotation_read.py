import json

s = '{"fires": null, "expenses": 14.99, "sales": [{"revenue": 100,
"day:": "Monday"}, {"revenue": 200, "day": "Tuesday"}, {"day":
"Wednesday", "holiday": true}]}'

print(sum([day for day in data['sales'] if 'revenue' in day.keys()]))


