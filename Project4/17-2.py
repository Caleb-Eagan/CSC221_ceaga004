from operator import itemgetter

import requests
import plotly.express as px

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts, comments, hover_texts = [], [], []
full_dict = {}

for submission_id in submission_ids[:30]:
    # Make a new API call and check the response
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    }
    try:
        submission_dict['comments'] = response_dict['descendants']
    except:
        submission_dict['comments'] = -1

    submission_dicts.append(submission_dict)
    comment = submission_dict['comments']
    comments.append(submission_dict['comments'])

    title = f"<a href='{submission_dict['hn_link']}''>{submission_dict['title']}</a>"
    hover_text = f"{submission_dict['title']}"
    hover_texts.append(hover_text)

    full_dict[title] = comment
    
full_dict = {key: val for key, val in
             sorted(full_dict.items(),key = lambda ele: ele[1], reverse=True)}

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

# Make visualization
title = "Most Active Discussions On Hacker News Currently"
labels = {'x': 'Submissions', 'y': 'Comments'}
fig = px.bar(x=full_dict.keys(), y=full_dict.values(), title=title, labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='Red', marker_opacity=0.6)

fig.show()
fig.write_html('17-2.html')