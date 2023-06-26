import asyncio
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs
from pyppeteer import launch
total_list = ["title", "time", "view"]
f = open('crawl.csv', 'w', encoding="utf-8", newline='')
wr = csv.writer(f)
wr.writerow([total_list[0], total_list[1], total_list[2]])
f.close()
async def main():
    i = 0
    while True:
        origin_df = pd.read_csv('crawl.csv', encoding='utf-8')
        login_url = 'https://nid.naver.com/nidlogin.login'
        id = ""
        pw = ""
        browser = await launch()
        page = await browser.newPage()
        await page.goto(login_url)
        await page.type('input[name="id"]', id)
        await page.type('input[name="pw"]', pw)
        await page.click('input[type="submit"]')
        await page.waitForNavigation()
        baseurl = 'https://cafe.naver.com/cafeurl'
        i = i + 1
        print(i)
        clubid = 13005023
        boardtype = "L"
        pageNum = i
        userDisplay = 50
        await page.goto(baseurl + 'ArticleList.nhn?search.clubid=' + str(clubid) + '&search.boardtype=' + str(
            boardtype) + '&search.page=' + str(pageNum) + '&userDisplay=' + str(userDisplay))
        await page.waitForSelector('#cafe_main')
        await page.switch_to_frame('cafe_main')
        soup = bs(await page.content(), 'html.parser')
        soup = soup.find_all(class_='article-board m-tcol-c')[1]
        datas = soup.select("#main-area > div:nth-child(4) > table > tbody > tr")
        for data in datas:
            article_title = data.find(class_="article")
            article_date = data.find(class_='td_date')
            article_view = data.find(class_='td_view')
            if article_title is None:
                article_title = "null"
            else:
                article_title = article_title.get_text().strip()
            if article_date is None:
                article_date = "null"
            else:
                article_date = article_date.get_text().strip()
            if article_view is None:
                article_view = "null"
            else:
                article_view = article_view.get_text().strip()
            f = open('crawl.csv', 'a+', newline='', encoding="utf-8")
            wr = csv.writer(f)
            wr.writerow([article_title, article_date, article_view])
            f.close()
        print('end')
        await browser.close()
asyncio.run(main())



