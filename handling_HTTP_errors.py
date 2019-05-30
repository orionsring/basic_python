
from urllib.error import HTTPError
url = 'http://codeschool.com/does_not_exist.html'
conn = urlopen(url)
try:
    conn = urlopen(url)
    conn.close()
except HTTPError as e:
    print(e.status)
    print(e.reason)




