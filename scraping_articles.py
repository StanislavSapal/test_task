import requests
from bs4 import BeautifulSoup
from scraping_urls import travel_urls
from prettytable import PrettyTable


def text_to_words_list(*args):
    """Функция принимает строки и списки строк и складывает все слова в единый список, очищая от знаков
    в конце каждого слова, если они есть"""

    words_list = []

    for arg in args:
        if isinstance(arg, str):
            words_list.extend(arg.split())
        elif isinstance(arg, list):
            for item in arg:
                words_list.extend(item.split())

    for i in range(len(words_list)):
        if words_list[i][-1] in ['.', ',', '!', '?', '...', ':']:
            words_list[i] = words_list[i][:-1]

    return words_list


def get_most_repeated_word(words_list):
    words_list = [word for word in words_list if word.lower() not in ['the', 'and', 'to', 'on', 'in', 'at', 'a', 'an',
                                                                      'of', 'from', 'is', 'with', 'will', 'are', 'for',
                                                                      'as', 'that', 'by']]
    word_count = {}
    max_count = 0
    most_repeated_word = ""

    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        if word_count[word] > max_count:
            max_count = word_count[word]
            most_repeated_word = word

    return most_repeated_word


table = PrettyTable()
table.field_names = ['Название статьи', 'Урл статьи', 'Количество слов', 'Количество абзацев', 'Количество изображений',
                     'Самое распространенное слово', 'Теги статьи']

for url in travel_urls:
    link = 'https://www.thenationalnews.com' + url
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    h1_text = soup.find('h1').text

    h2_tags = soup.findAll('h2')
    h2_text = [elem.text for elem in h2_tags]

    p_tags = soup.findAll('p')
    p_text = [elem.text for elem in p_tags]

    words_in_article_list = text_to_words_list(h1_text, h2_text, p_text)

    images = soup.findAll('figure')

    paragraph_quantity = len(p_tags) - len(images)  # под каждым изображением есть текст, который по сути
                                                    # абзацем не является.
    tag_blocks = soup.find('div', class_='default__TagsHolder-a1tih0-0 dlTgjK tags-holder margin-sm-bottom').findAll('a')
    tags = [tag.text for tag in tag_blocks]

    table.add_row([h1_text, link, len(words_in_article_list), paragraph_quantity, len(images),
                   get_most_repeated_word(words_in_article_list), tags])

print(table)
