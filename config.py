from requests import Session
from requests.auth import HTTPBasicAuth
import secret

# URLs used for various API calls
base_url = 'https://bbisec02pro.blackbaudhosting.com'
database_name = '1234ABC_fbd2546c-1d4d-4508-812c-5d4d915d856a'
appfx = '/AppFxWebService.asmx'
api = f'{base_url}{database_name}{appfx}'
base_endpoint = 'Blackbaud.AppFx.WebService.API.1/'

username, password = secret.get_secret()
username = 'BLACKBAUDHOST\\' + username

session = Session()
session.auth = HTTPBasicAuth(username, password)

headers = {'Content-Type': 'text/xml; charset=utf-8',
           'Host': 'bbisec04pro.blackbaudhosting.com',
           'SOAPAction': ''}
