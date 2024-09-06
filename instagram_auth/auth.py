import requests
import time

username = YOURT_USERNAME
password = YOUR_PASSWORD

session = requests.Session()
session.get('https://www.instagram.com/')
enpw = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
csrf = session.cookies['csrftoken']

res = session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', 
    data={
        'username': username,
        'enc_password': enpw,
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    },
    headers={
        'X-CSRFToken': csrf,
    }
).json()

if res.get('authenticated'):
    user_id = res['userId']
    
    print(user_id)
else:
    print('Authentication failed')
