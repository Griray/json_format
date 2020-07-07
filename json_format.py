import json
from pprint import pprint
from collections import Counter


with open("newsafr.json", encoding="utf-8") as f:

    all_words = []
    pop_words = []

    json_data = json.load(f)
    for item in json_data['rss']['channel']['items']:
        news = item['description']
        news = news.lower()
        news = news.split()


        all_words.extend(news)

    for word in all_words:
        if len(word) > 6:
            pop_words.append(word)

    stat = Counter(pop_words)
    print("ТОП 10 слов", stat.most_common(10))

