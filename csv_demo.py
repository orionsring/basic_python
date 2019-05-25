import app

app.generate_row()

app.generate_rows(2, 4)

ps_data= open('ps_data.csv', 'w')

import csv 

wtr = csv.writer(ps_data)

wtr.writerrow(app.generate_row())

wtr.writerows(app.generate_rows(1, 5))

ps_data.close()
