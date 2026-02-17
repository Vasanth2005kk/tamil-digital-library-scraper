
from time import time
from tkinter.filedialog import test
from openpyxl import Workbook
from Details import get_book_details
import os

file_name = "Books_Details.xlsx"
count = 0
All_Boolk_links = "books.txt"

# Create new excel file
wb = Workbook()
ws = wb.active
ws.title = "Books"

# Header row
ws.append(["S.No", "Book Name", "Book Link", "Author", "Edition Year", "Category", "Tag", "Publisher", "Document Location", "Book Download Link"])


if __name__ == "__main__":    
    try:
        with open(All_Boolk_links, "r", encoding="utf-8") as f:
            for line in f:
                book_url = line.strip()
                if not book_url:
                    continue
                count += 1
                book_details = get_book_details(book_url, s_no=count)
                if book_details:
                    ws.append(list(book_details.values()))
                
                # test with 5 books only
                if count == 5 :
                    break

    except FileNotFoundError:
        print(f"[-] Error: {All_Boolk_links} not found.")
        
        # Save file even if no books were scraped
    if os.path.exists(file_name):
        print(f"[-] Warning: {file_name} already exists and will be overwritten.")
        file_name = f"Books_Details_{int(time())}.xlsx"
    wb.save(file_name)

    print(f"Excel file created: {file_name}")