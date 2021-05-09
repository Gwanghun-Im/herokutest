import requests
import re

def user(u):
    req = requests.get(f'https://api.github.com/users/{u}/repos')
    req_to_json = req.json()
    repo_list = [i.get('name') for i in req_to_json]
    total_commit = 0

    for repo in repo_list:
        total_commit += int(commitCount(u,repo))
    return total_commit

def commitCount(u, r):
    return re.search('\d+$', requests.get(f'https://api.github.com/repos/{u}/{r}/commits?per_page=1').links['last']['url']).group()

u = input('유저 이름을 입력해')
print(u, user(u))