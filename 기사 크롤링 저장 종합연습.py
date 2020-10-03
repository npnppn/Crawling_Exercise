from bs4 import BeautifulSoup
from selenium import webdriver
from openpyexcel import Workbook

# 엑셀로 저장하는 코드
wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

# 크롤링 설정
driver = webdriver.Chrome('chromedriver')
url = f"https://search.naver.com/search.naver?&where=news&query=추석"
driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

# 크롤링 시작
for article in articles:
    #print(article)
    title = article.select_one("dl > dt > a").text
    url = article.select_one("dl > dt > a")['href']
    comp = article.select_one("span._sp_each_source").text.split(" ")[0].replace("언론사", "")
    thumbnail = article.select_one("img")['src']
    print(title, url, comp, thumbnail)
    ws1.append([title, url, comp, thumbnail])
wb.save(filename='articles.xlsx')
driver.quit()
