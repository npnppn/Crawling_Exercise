from bs4 import BeautifulSoup
from selenium import webdriver
from openpyexcel import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    comp = article.select_one("span._sp_each_source").text.split(' ')[0].replace('언론사','')
    ws1.append([title, url, comp])

    #print(title, url, comp)
    #print(comp)

driver.quit()
wb.save(filename='articles.xlsx')
