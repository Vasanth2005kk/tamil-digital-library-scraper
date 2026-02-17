import requests
from bs4 import BeautifulSoup

def get_book_details(book_url, s_no):
    """
    Fetches and extracts book details from a given URL.
    Returns a dictionary of details or None if failed.
    """
    try:
        # 1. Fetch the page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Added timeout to prevent hanging
        response = requests.get(book_url, headers=headers, timeout=15)

        if response.status_code != 200:
            print(f"[-] Request Failed for {book_url}: Status {response.status_code}")
            return None

        # Force UTF-8 encoding to prevent Unicode errors
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Main container
        book_details = soup.find("div", class_="card p-7 border-bottom mb-5")
        if not book_details:
            print(f"[-] Could not find book details for index {s_no}")
            return None

        # --- Data Extraction with Safety Checks ---

        # 1. Extract Title
        title_tag = book_details.find("h5")
        title = title_tag.get_text(strip=True) if title_tag else None

        # 2. Extract Author
        author_tag = book_details.find("p", class_="fs-6 mb-0 text-primary-link")
        author_name = author_tag.get_text(strip=True) if author_tag else None

        # 3. Extract Publisher
        publisher_names = None
        publisher_div = book_details.find("div", itemprop="publisher")
        if publisher_div:
            publisher_links = publisher_div.find_all("a", itemprop="url")
            if publisher_links:
                publisher_names = ", ".join([link.get_text(strip=True) for link in publisher_links])

        # 4. Extract Year
        # d-flex flex-wrap mb-3
        year  = None
        year_tag = book_details.find_all("div", class_="d-flex flex-wrap mb-3")
        if year_tag:
            # print(f"Year Tag Found: {year_tag}")
            year = year_tag[2].find('p', class_="fs-6 mb-0")
            if year:
                year = year.get_text(strip=True)

        # 5. Extract Location
        location_tags = book_details.find_all("p", class_="fs-6 mb-0")
        location = location_tags[-1].get_text(strip=True) if location_tags else None
        
        # 6. Extract Category 
        category_tags = book_details.find_all('p', class_="fs-6 mb-0 text-primary-link")
        category = category_tags[-1].get_text(strip=True) if category_tags else None

        # 7. Extract Tags
        tags = None
        tag_ul = book_details.find("ul", class_="d-flex flex-wrap mb-0 mt-2 gap-2 ps-0")
        if tag_ul:
            labels = tag_ul.find_all('label')
            if labels:
                tags = ", ".join([label.get_text(strip=True) for label in labels])
    
        # 8. Download Link
        book_download_url = None

        download_div = soup.find("object", class_="pdf container-fluid px-0 py-10")
        book_download_url = download_div.get("data",None)

        # 2. Logging and Return
        print(f"[+] Scraping S.No {s_no}: {title if title else 'Unknown'}")
        
        return {
            "S.No": s_no,
            "Title": title,
            "Book Link": book_url,
            "Author": author_name,
            "Year": year,
            "Category": category,
            "Tag": tags,
            "Publisher": publisher_names,
            "Location": location,
            "Download Link": book_download_url
        }

    except Exception as e:
        print(f"[-] Error scraping index {s_no}: {e}")
        with open("Feil.txt", "a", encoding="utf-8") as error_file : 
            error_file.write(f"Error scraping index {s_no} for URL  : {book_url}\n")
        return None


if __name__ == "__main__":
    # For testing one book:
    test_url = "https://tamildigitallibrary.in/Articles/062714_%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D%E0%AE%95%E0%AF%8D_%E0%AE%95%E0%AE%B5%E0%AE%BF%E0%AE%A4%E0%AF%88%E0%AE%AF%E0%AE%BF%E0%AE%B2%E0%AF%8D_%E0%AE%AA%E0%AE%BE%E0%AE%B0%E0%AE%A4%E0%AE%BF%E0%AE%AF%E0%AE%BF%E0%AE%A9%E0%AF%8D_%E0%AE%A4%E0%AE%BE%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D"
    details = get_book_details(test_url, s_no=1)
    print(details)