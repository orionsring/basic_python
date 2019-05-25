import app

app.generate_row()

app.generate_rows(2, 4)

ps_data= open('ps_data.csv', 'w')

import csv 

wtr = csv.writer(ps_data)

wtr.writerrow(app.generate_row())

wtr.writerows(app.generate_rows(1, 5))

ps_data.close()

#!more ps_data.csv  OR !cat ps_data.csv ON APPLE

#!del ps_data.csv   OR !rm ps_data.csv  ON APPLE 

ps_data = open('ps_data.csv', 'w')

dw = csv.DictWriter(ps_data, fieldnames=app.HEADERS)

dw.writeheader()

first = dict(zip(app.HEADERS, app.generate_row()))
#zip(['a', 'b', 'c'], [1, 2, 3])
#[('a', '1'), ('b', '2'), ('c', '3')]

first 
#{'first_name': 'Deborah',
# 'last_name':  'Kurata'
# 'title':      'Angular 2: Getting started',
# 'votes':      891}

rows = [dict(zip(app.HEADERS, row)) for row in app.generate_rows(0, 5)]

dw.writerow(rows[0])
#47

second = rows[1]

second['foo'] = 'bar'

second
#{'first_name': 'Scott',
# 'foo':        'bar',
# 'last_name':  'Allen',
# 'title':      'C# Fundamentals with Visual Studio 2015',
# 'votes':      1979

#dw.writerow(second)
# you should get a very long error here***

second.pop('foo', None)
#'bar'

dw.writerow(second)
#error gone here ***
#58

third = rows[2]

third.pop('title', None)
#'Angular 2 Fundamentals'

dw.writerow(third)
#17

dw.writerows(rows[3:])

ps_data.close()

#!cat ps_dat.csv

ps_data = open('ps_data.csv', 'r')

rdr = csv.reader(ps_data)

for row in rdr:
    print(row)
	
ps_data.seek(0)
#0

dr = csv.DictReader(ps_data)

for row in dr:
    print(row)


