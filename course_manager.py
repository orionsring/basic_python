from urllib.request import Request, urlopen
import json
APPLICATION_ID = '82e58e45-694d-438e-b80f-44888d4573ce'
REST_API_KEY = 'p0Fiv8szIhCnUCK7Mfug2zeV0YU9UwTe'

BASE_URL = 'https://parse.buddy.com/parse'

CLASSES = '/classes'
CLASS_COURSE = '/course'

PARSE_HEADERS = {
    'X-Parse-Application-Id': APPLICATION_ID,
    'X-Parse-REST-API-Key': REST_API_KEY,
    'Content-Type: 'application/json'
}

def create_course(title, author_first_name, author_last_name):
    url = BASE_URL + CLASSES + CLASS_COURSE

    data = {
        'title': title,
        'author_first_name': author_first_name,
        'author_last_name': author_last_name,
        'votes': 0,
		'stars': 0
}

    q = Request(url, method='POST', headers=PARSE_HEADERS, data=json.dump(data).encode('utf-8'))
    conn = urlopen(q)
    s_data = ''.join([line.decode('utf-8') for line in col])
    result = json.loads(s_data)
    
    print(result)

if __name__ == '__main__':
    create_course('Getting Started with teh Python Standard Library'', 'Douglas', 'Starnes')



