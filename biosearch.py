import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def __crawler_article__(url):
    response = requests.get(url)
    soup = bs(response.content, "html.parser")

    status = response.status_code
    if status >= 300:
        print(f"Error: {status}")
        return []

    articles = []

    for article in soup.find_all('article', class_="full-docsum"):
        title_tag = article.find('a', class_='docsum-title')
        authors_tag = article.find('span', class_='docsum-authors')
        PMID_tag = article.find('span', class_='docsum-pmid')

        title = title_tag.text.strip() 
        authors = authors_tag.text.strip()
        PMID = PMID_tag.text.strip()

        paper_url = "https://pubmed.ncbi.nlm.nih.gov/" +"/"+str(PMID)+"/"
        paper = requests.get(paper_url)
        detail = bs(paper.content, "html.parser")
        paper_link = detail.find('a', class_='id-link')['href']



        articles.append({
            'title': title,
            'authors': authors,
            'pmid': PMID,
            'link': paper_link
        })

    return articles



