import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
res = requests.get(url)
print(f'Status code: {res.status_code}')

submission_ids = res.json()

submission_dicts = []
for submission_id in submission_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    res = requests.get(url)
    print(f'Status code: {res.status_code}')
    response_dict = res.json()
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=lambda x: x['comments'], reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")