# Daily views on the Python (programming language) wikipedia page

# I spent way too much time trying to figure this out lmao

import requests
import plotly.express as px


# Make an API call and check the response
url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Python_(programming_language)/daily/20240101/20240131"
headers = {'User-Agent': 'Wikipedia Data Analysis (ceaga004@plattsburgh.edu)'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# Process information about each submission
data = r.json()
items = data['items']

days, views= [], []
full_dict = {}

for item in items:
    date = item['timestamp']
    date_list = []

    for i in date:
        date_list.append(i)

    day = f'{date_list[6]}{date_list[7]}'
    days.append(f"January {day}")

    view_count = item['views']
    views.append(view_count)


# Make visualization
title = "Pageviews of the Python (programming language) article on Wikipedia during January 2024"
labels = {'x': 'Day', 'y': 'Views'}
fig = px.bar(x=days, y=views, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='Red', marker_opacity=0.6)

fig.show()
fig.write_html('wikipedia_python_page_views.html')