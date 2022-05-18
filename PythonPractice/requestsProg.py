from asyncio.windows_events import NULL
from urllib import request
import requests

req = requests.get('https://api.github.com/users/naveenkrnl')

print(req)
#print(req.content)

response=req.json()
for key,value in response.items():
    if key == 'login' && value == 'naveenkrnl':
        print(response['id'],'=', value)
