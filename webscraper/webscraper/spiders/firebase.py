import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from webspider import run_spider
import time
import schedule


db = firestore.client()

def run_and_store_spider():
    # Run the spider and get the scraped data
    scraped_data = run_spider()

    # Set the scraped data in Firestore
    doc_ref = db.collection(u'scholarships').document(u'new')
    doc_ref.set(scraped_data)
    


# Schedule the spider to run every 7 days
schedule.every(0).minutes.do(run_and_store_spider)

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)
