
import httpx

r = httpx.get('https://www.python.org')
print(r.status_code)
print(r.text[:1000])
