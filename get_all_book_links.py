from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

url = "https://tamildigitallibrary.in/book-search-new?sub_cat_id=5&cat_id=20&sub_cat_name=நாட்டிமை நூல்"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

time.sleep(5)  # wait for JS load

# Add new option 5044 and select it
driver.execute_script("""
let select = document.getElementById("pagination_length");

let option = document.createElement("option");
option.value = "5044";
option.text = "5044";
select.appendChild(option);

select.value = "5044";
select.dispatchEvent(new Event("change"));
""")

time.sleep(8)  # wait data load

links = driver.find_elements(By.TAG_NAME, "a")

book_links = []

for link in links:
    href = link.get_attribute("href")
    if href:
        if href not in book_links:
            book_links.append(href)
driver.quit()

with open("books.txt", "w", encoding="utf-8") as f:
    for i, book in enumerate(book_links, start=1):
        if "Articles" in book:
            print(i, book)
            f.write(book + "\n")

print("Saved into books.txt")

