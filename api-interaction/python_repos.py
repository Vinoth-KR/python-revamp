import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python&sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
response_dict = r.json()

print(f'Total repositories: {response_dict["total_count"]}')
print(f'Complete results: {not response_dict["incomplete_results"]}')

repo_dicts = response_dict['items']
print(f'Number of repositories returned: {len(repo_dicts)}')

repo = repo_dicts[0]
print(f'\nKeys: {len(repo_dicts[0])}')
for key in sorted(repo.keys()):
    print(key)