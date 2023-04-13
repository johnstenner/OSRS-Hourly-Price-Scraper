import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Provide a list of item IDs
item_ids = []  # Add more item IDs as needed

def get_item_buy_price(item_id):
    url = f"https://prices.runescape.wiki/osrs/item/{item_id}"

    # Set up Selenium WebDriver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    try:
        # Locate the buy price element using its class name
        buy_price_element = driver.find_element(By.CSS_SELECTOR, "span.wgl-item-price")

        # Extract the buy price
        buy_price = buy_price_element.text
        print(f"Item ID: {item_id} - Current buy price: {buy_price}")

    finally:
        # Close the browser window
        driver.quit()

    return buy_price

def job(item_ids):
    print(f"Running the scraper at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    for item_id in item_ids:
        get_item_buy_price(item_id)


# Schedule the scraper to run every hour
schedule.every(1).hours.do(job, item_ids)

# Run the scraper indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
