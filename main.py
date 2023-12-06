import requests


def requestit():
    res = requests.get('https://adventofcode.com/2023/day/1/input')
    print(res.text)
    print(res.status_code)

if __name__ == '__main__':
    requestit()