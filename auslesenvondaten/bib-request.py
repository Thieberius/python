import requests
r = requests.get('http://www.example.com/')
print(r.text)
print(r.status_code)
r = requests.get('https://www.python-lernen.de/bilder/biene-sprite-animiert-01.gif')
print(r.content)
with open('biene.gif', 'wb') as f:
    f.write(r.content)
payload = {'key1': 'value!', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
r = requests.get('http://httpbin.org/basic-auth/a/b', auth=('a', 'b'))
print(r.text)
print(r.ok)
print(r.headers)
