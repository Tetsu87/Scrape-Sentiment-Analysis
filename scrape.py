import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

url = 'https://www.aljazeera.com{}'
base_url = url.format('/where/mozambique/')
res = requests.get(base_url)

soup = BeautifulSoup(res.text, "html.parser")
elems = soup.find_all('a', class_='u-clickable-card__link')
links = []
data = []
f = open('output.json', 'w')

for elem in tqdm(elems[:10]):
   # url of each article
    link = elem.attrs['href']
    target_url = url.format(link)

    # response to each article
    target_res = requests.get(target_url)
    target_soup = BeautifulSoup(target_res.text, "html.parser")

    # scrape a title
    title = target_soup.find('h1')
    if title != None:
        title = title.text

    # scrape a subtitle
    subtitle = target_soup.find('em')
    if subtitle != None:
        subtitle = subtitle.text

    # scrape contents
    contents = target_soup.find('div', class_='wysiwyg')
    if contents != None:
        contents = contents.text

    # scrape an image
    image = target_soup.find('img')
    image_url = image.get('src')

    # scrape a fig_caption
    figcaption = target_soup.find('figcaption')
    if figcaption != None:
        figcaption = figcaption.text

    # scrape a published date
    date = target_soup.find('div', class_='date-simple')
    display_date = date.find_all('span')
    if display_date != None:
        display_date[1] = display_date[1].text

    # scrape a source
    source = target_soup.find('div', class_='article-source')
    if source != None:
        source = source.text[8:]

    result = {'title': '', 'subtitle': '', 'contents': '',
              'image': '', 'figcaption': '', 'date': '', 'source': ''}
    result.update(title=title, subtitle=subtitle, contents=contents, image=url.format(
        image_url), figcaption=figcaption, date=display_date[1], source=source)
    data.append(result)

json.dump(data, f, indent='\t')
