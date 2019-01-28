# Darren Coughlan - 13305471
# Part 1

import urllib
import bs4
import os

link = "http://mlg.ucd.ie/modules/COMP41680/archive/"
response = urllib.request.urlopen(link + "index.html")
html = response.read()
parser = bs4.BeautifulSoup(html, 'html.parser')

# print(parser)

# Get list of URLs for each month
months = []
for match in parser.find_all("a"):
    months.append(match.get('href'))

# Remove empty stings from the months urls
while '' in months:
    months.remove('')

try:
    os.stat('Categories')
except:
    os.mkdir('Categories')

# Get articles and categories from each month's news link
articles = []
categories = []
f = open("Categories\\Categories.txt", "w", encoding="utf-8")
for n in range(0,12):
    link_month = link+months[n]
    response_month = urllib.request.urlopen(link_month)
    html = response_month.read()
    parser = bs4.BeautifulSoup(html, 'html.parser')
    for match in parser.find_all("a"):
        if "article" not in match.get('href'):
            continue
        else:
            articles.append(match.get('href'))

    for match in parser.find_all("td", class_='category'):
        if "N/A" not in match.get_text():
            f.write(match.get_text()+"\n")
    print("Categories %d" %n)
f.close

# Function to return article text and heading
def save_text(article_url):
    response = urllib.request.urlopen(article_url)
    html = response.read()
    parser = bs4.BeautifulSoup(html, 'html.parser')
    text = ""
    # print(parser)
    for match in parser.find_all("h2"):
        text = match.get_text()
    for match in parser.find_all("p"):
        if match.get_text() == "Return to article search results":
            continue
        else:
            text = text+"\n"+match.get_text()
    return text

try:
    os.stat('Article_text_files')
except:
    os.mkdir('Article_text_files')

for n in range(0,len(articles)):
    text = save_text(link+articles[n])
    f = open("Article_text_files\\"+str(n)+"_article.txt", "w", encoding="utf-8")
    print(articles[n], " saved")
    f.write(text)
    f.close()
