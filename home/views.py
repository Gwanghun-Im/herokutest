from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        username = request.GET.get('username')
        context = {
            'username':username,
            'cnt':who(username)
        }
        return render(request, 'home/index.html',context)
    except:
        return render(request, 'home/index.html')

import requests
import re

def who(u):
    req = requests.get(f'https://api.github.com/users/{u}/repos')
    req_to_json = req.json()
    repo_list = [i.get('name') for i in req_to_json]
    total_commit = 0

    for repo in repo_list:
        total_commit += int(commitCount(u,repo))
    return total_commit

def commitCount(u, r):
    return re.search('\d+$', requests.get(f'https://api.github.com/repos/{u}/{r}/commits?per_page=1').links['last']['url']).group()
