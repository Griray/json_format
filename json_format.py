import json
from pprint import pprint
from collections import Counter


with open("newsafr.json", encoding="utf-8") as f:

    all_words = []
    pop_words = []

    json_data = json.load(f)
    for item in json_data['rss']['channel']['items']:
        news = item['description'].lower()
        news = item['description'].split()
        all_words.extend(news)
    for word in all_words:
        if len(word) > 6:
            pop_words.append(word)

    stat = Counter(pop_words)
    sort_stat = sorted(((say, number) for say, number in stat.items()), key=lambda pair: pair[1], reverse=True)
    print("Топ 10 слов в новостной ленте: ")
    for i in range (10):
        print(sort_stat[i])
