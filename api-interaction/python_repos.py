import requests
import plotly.express as px

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

repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # print(f'Name: {repo_dict["name"]}')
    # print(f'Owner: {repo_dict["owner"]["login"]}')
    # print(f'Stars: {repo_dict["stargazers_count"]}')
    # print(f'Repository: {repo_dict["html_url"]}')
    # print(f'Description: {repo_dict["description"]}')
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f'{owner}<br>{description}'
    hover_texts.append(hover_text)


#Visualization
title = 'Most-Starred Python Projects on GitHub'
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=18, yaxis_title_font_size=18)
fig.show()
