import requests

resp = requests.get("https://github.com/")

print(f'Status code: {resp.status_code}')
print(f'Header: {resp.headers}\n')
print(f'Content: {resp.content}')