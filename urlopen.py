
from urllib.request import urlopen
conn = urlopen('http://codeschool.com')
conn.status
conn.reason
lines = conn.readlines()
data=''.join([line.decode('utf-8') for line in lines])
# do something with the data
conn.close()




	
	
	


