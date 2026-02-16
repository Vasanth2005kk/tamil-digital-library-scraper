# Tamil Digital Library Scraper

This project is a simple and powerful tool to scrape book details from the [Tamil Digital Library](https://tamildigitallibrary.in/). It extracts information for a total of **5,044 books** and saves them into an Excel file.

## 🚀 Features
- **Total Books:** Scrapes details for all 5,044 books.
- **Data Extracted:** Title, Author, Year, Category, Tags, Publisher, Location, and Download Link.
- **Output:** Saves everything into an easy-to-read Excel file (`Books_Details.xlsx`).

## 🛠️ Requirements
Before running the scripts, make sure you have the following installed:
- Python 3.x
- Selenium
- BeautifulSoup4
- Requests
- Openpyxl
- WebDriver Manager

You can install the dependencies using:
```bash
pip install selenium beautifulsoup4 requests openpyxl webdriver-manager
```

## 📂 Project Structure
- `get_all_book_links.py`: Uses Selenium to fetch all 5,044 book URLs from the website.
- `Details.py`: The core logic to scrape specific details from each book page.
- `main.py`: The main script that reads links from `books.txt` and saves details to Excel.
- `books.txt`: A text file containing all the collected book URLs.
- `Books_Details.xlsx`: The final generated Excel file.

## 📖 How to Use

### Step 1: Get Book Links
Run the first script to collect all book URLs from the library:
```bash
python get_all_book_links.py
```
This will create a `books.txt` file with 5,044 links.

### Step 2: Extract Details
Run the main script to start scraping details for each book:
```bash
python main.py
```
This script will read `books.txt`, visit each page, and save the data to `Books_Details.xlsx`.

## ⚙️ How it Works (Scraping Method)
The scraper uses a two-step process:
1. **Link Collection:** Since the website uses dynamic loading, we use **Selenium** to interact with the search page. We inject a custom script to set the pagination to **5,044**, allowing us to see and grab all links at once.
2. **Data Extraction:** Once we have the links, we use **BeautifulSoup** and **Requests** for fast and efficient data extraction from each individual book page.

---
*Created with ❤️ for the Tamil Digital Library project.*
