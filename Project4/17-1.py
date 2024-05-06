import requests
import plotly.express as px
import numpy as np

# Make an API call and check the response


languages = ['python','java','javascript','ruby','c','perl','go','haskell','vb','kotlin']

repo_links, most_popular_projects, hover_texts = [], [], []
full_dict = {}

for language in languages:
    url = "https://api.github.com/search/repositories"
    url += f"?q=language:{language}+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    print(language)

    # Process overall results
    response_dict = r.json()
    print(f"Complete results: {not response_dict['incomplete_results']}")

    # Process repository information
    repo_dict = response_dict['items'][0]
    
    # Turn repo name into active link
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars = repo_dict['stargazers_count']
    most_popular_projects.append(stars)

    # Build hover texts
    language = repo_dict['language']
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{language}<br />{owner}<br />{description}"
    hover_texts.append(hover_text)
    full_dict[repo_link] = stars
    
full_dict = {key: val for key, val in sorted(full_dict.items(), key = lambda ele: ele[1], reverse=True)}

# Make visualization
title = "Most-Starred Project From 10 Different Coding Languages On GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=full_dict.keys(), y=full_dict.values(), title=title, labels=labels,
             hover_name=hover_texts)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_layout(yaxis={'categoryorder':'total ascending'}) # add only this line

fig.show()
fig.write_html('17-1.html')