import requests

base_url = 'http://your-web-app.com'

# endpoint
endpoints = [
    '/home',
    '/products',
    '/contact'
]

# number of requests to send
num_requests = 100

# Loop through each endpoint and send HTTP GET requests
for endpoint in endpoints:
    for _ in range(num_requests):
        url = base_url + endpoint
        response = requests.get(url)
        print(f'Request to {url} - Status Code: {response.status_code}')
