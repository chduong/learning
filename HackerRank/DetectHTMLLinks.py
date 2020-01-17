import sys
from bs4 import BeautifulSoup
from xml.sax.saxutils import escape

n = int(input())
page = sys.stdin.read()

soup = BeautifulSoup(page, 'html.parser')
links = []
for link in soup.findAll('a'):
    links.append([escape(link.get('href')), link.text.strip()])

for i in range(len(links)):
    print('{l},{t}'.format(l=links[i][0], t=links[i][1]))

###############################
# from bs4 import BeautifulSoup
# from xml.sax.saxutils import escape
#
# f = open('data/input.txt', 'r')
# n = int(f.readline())
# page = f.read()
# f.close()
#
# soup = BeautifulSoup(page, 'html.parser')
# links = []
# for link in soup.findAll('a'):
#     links.append([escape(link.get('href')), link.text.strip()])
#
# for i in range(len(links)):
#     print('{l},{t}'.format(l=links[i][0], t=links[i][1]))

###############################
# import re
#
# def detect_links(html):
#     links = re.findall(r'<\s*a [^>]*href="([^"]*)"[^>]*>(.*?)</a', html)
#     return ((href.strip(), re.sub('<[^>]*>', '', title.strip())) for href, title in links)
#
# if __name__ == '__main__':
#     import sys
#     for link, text in detect_links(sys.stdin.read()):
#         print('{},{}'.format(link, text))

###############################
# from bs4 import BeautifulSoup
# from xml.sax.saxutils import escape
#
# def detect_links(html):
#     soup = BeautifulSoup(html, "html")
#     links = soup.find_all('a')
#     return ((escape(link.get('href')), link.text.strip()) for link in links)
#
# if __name__ == '__main__':
#     import sys
#     for link, text in detect_links(sys.stdin.read()):
#         print('{},{}'.format(link, text))