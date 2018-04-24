"""
http://docs.python-requests.org/en/master/
r = requests.get('http://httpbin.org/get', params = {'key1': 'key1', 'key2': 'key2'})
print(r.url) - http://httpbin.org/get?key1=key1&key2=key2

parametry które są ustawione jako None nie zostaną przekazane
r = requests.get('http://httpbin.org/get', params = {'key1': 'key1', 'key2': None})
print(r.url) - http://httpbin.org/get?key1=key1

przekazywanie parametrów jako lista
r = requests.get('http://httpbin.org/get', params = {'key1': 'value1', 'key2[]': ['value2', 'value3']})
print(r.url) http://httpbin.org/get?key1=value1&key2%5B%5D=value2&key2%5B%5D=value3

r.text
r.status_code
r.raise_for_status()
r.json() - jeśli nie uda zdekodować do jsona to zwrócony zostanie błąd ValueError: No JSON object could be decoded

dodawanie headers:
headers = {'user-agent': 'my-app/0.0.1'}
url = 'https://api.github.com/some/endpoint'
r = requests.get(url, headers=headers)

application/x-www-form-urlencoded
jeśli chcemy wysłać formularz html (form-encoded) to wystarczy użyć
payload = {'key1': 'value1', 'key2': 'value2'}
requests.post("http://httpbin.org/post", data=payload)
wtedy automacztynie payload zostanie przekonwertowany na form-encoded

jeśli w post jest wiele elementów o tym samym kluczu możemy użyć tupoli
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)

przesyłanie jako Content-Type:application/json wystarczy ustawić parametr json
url = 'https://www.komputronik.pl/frontend-api/customer/sign-in'
payload = {'customer_login': 'ss', 'customer_password': 'sss'}
r = requests.post(url, json=payload)

pobieranie ciasteczek r.cookies r.cookies['KTRSESSION']
"""
import requests

# url = 'https://www.komputronik.pl/frontend-api/customer/sign-in'
# payload = {'customer_login': 'ss', 'customer_password': 'sss'}
# cookies = dict(cookies_are='working')
# r = requests.post(url, cookies=cookies)
# print( r.headers)

headers = {'user-agent': 'my-app/0.0.1'}
url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'
r = requests.get(url, headers = headers)
print(r.headers)

