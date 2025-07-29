import scrapy
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.crawler import CrawlerProcess
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firestore
# Use a service account
cred = credentials.Certificate('Creden For FireBase')

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

class WebspiderSpider(scrapy.Spider):
    name = "webspider"
    start_urls = [
        "https://www.ilmkidunya.com/scholarships/scholarships-in-canada.aspx",
        "https://www.ilmkidunya.com/scholarships/scholarships-in-united-kingdom.aspx",
        "https://www.ilmkidunya.com/scholarships/scholarships-in-united-states.aspx",
        "https://www.ilmkidunya.com/scholarships/scholarships-in-france.aspx",
        "https://www.ilmkidunya.com/scholarships/scholarships-in-germany.aspx"
    ]

    def __init__(self, *args, **kwargs):
        super(WebspiderSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        self.driver.get(response.url)

        while True:
            try:
                # Find and click the "Load More" button by its id
                button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'A2')))
                button.click()
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loading-spinner')))
            except Exception as e:
                print("No more pages to load")
                break

        # Scrape the page after loading all content
        html = self.driver.page_source

        sel_response = scrapy.http.HtmlResponse(url=response.url, body=html, encoding='utf-8')
        for job in sel_response.css('.single-job'):
            scholarship_name = job.css('.job-title h3::text').get()
            deadline = job.css('.job-dates p:nth-child(2)::text').get()
            degree = job.css('.info-bottom p:nth-child(2) span::text').get()
            university_name = job.xpath(".//div[@class='job-list']/ul/li/div[@class='list-col'][3]/text()").get()
            level = job.xpath(".//div[@class='job-list']/ul/li[3]/div[@class='list-col'][3]/text()").get()
            country = job.xpath(".//div[@class='job-list']/ul/li[7]/div[@class='list-col'][3]/text()").get()

            scholarship = {
                'scholarship_name': scholarship_name,
                'deadline': deadline,
                'degree': degree,
                'university_name': university_name,
                'level': level,
                'country': country,
            }

            # Store the scholarship in Firestore
            doc_ref = db.collection(u'scholarships').document()
            doc_ref.set(scholarship)

            yield scholarship

    def closed(self, reason):
        self.driver.quit()

def run_spider():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0',
    })
    process.crawl(WebspiderSpider)
    process.start()  # the script will block here until the spider is finished
    process.stop()  # stop the Twisted reactor
