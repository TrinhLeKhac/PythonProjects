import requests
from plotly.graph_objs import Bar
from plotly import offline


# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, repo_links, stars, labels = [], [], [], []

for repo_dict in repo_dicts:

    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_url}</a>"

    repo_links.append(repo_link)
    repo_names.append(repo_name)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Started Python Projects on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}},
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}},
}

offline.plot({'data': data, 'layout': my_layout}, filename='python_repos.html')

# for repo_dict in repo_dicts:
#     print(f"\nSelected information about the first repository")
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")

