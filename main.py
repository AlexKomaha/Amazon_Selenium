# Run script /Library/Frameworks/Python.framework/Versions/3.11/bin/python3 /Users/alexkomaha/Desktop/Selenium/main.py


from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://www.amazon.co.jp/s?k=new+balance+shoes+summer&crid=3L2ZE7O6S97GX&sprefix=new+balance+shoes+summe%2Caps%2C217&ref=nb_sb_noss")

# pagination

isNextDisabled = False

while not isNextDisabled:

    elem_list = browser.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
    items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')


# print(len(items))

    for item in items:
        title = item.find_element(By.TAG_NAME, 'h2').text
        link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute("href")
        price = "No Price Found"

        try:
            price = item.find_element(By.CSS_SELECTOR, '.a-price').text
        except:
            pass

        image = "No Image Found"
        try:
            image = item.find_element(By.CSS_SELECTOR, '.s-image').get_attribute("src")
        except:
            pass

        print("Title: " + title)
        print("Price: " + price)
        print("Image: " + image)
        print("Page: " + link + '\n')

        browser.find_element(By.CLASS_NAME, 's-pagination-item').click
