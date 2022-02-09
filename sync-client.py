import time
import requests


def get_request(no):
    response = requests.get(f'http://localhost:9999/{no}')
    content = response.text
    print(f"{time.strftime('%X')} - {response.status_code} {content}")
    return content

def run():
    tasks = []
    print(f"{time.strftime('%X')} - Start")

    results = []
    for n in range(10):
        result = get_request(n)
        results.append(result)
    print('results:', results)

    print(f"{time.strftime('%X')} - Finish")


run()

