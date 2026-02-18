import requests
from tqdm import tqdm
import subprocess
import re

def download_books(Book_name, url , num):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        chunk_size = 1024  # 1KB

        with open(Book_name + ".pdf", "wb") as file, tqdm(
            desc="Downloading",
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:

            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))

        print(f"✅ {num} Successfully downloaded {Book_name}.pdf")
    else:
        print(f"❌ {Book_name} Failed to download file. Status code: {response.status_code}")


all_book_bytes = []

def chacking_size(url, num):
    command = ["curl", "-sI", "-L", "--max-time", "10", url]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        headers = result.stdout

        match = re.search(r"Content-Length:\s*(\d+)", headers, re.IGNORECASE)

        if match:
            size_bytes = int(match.group(1))
            all_book_bytes.append(size_bytes)

            size_mb = size_bytes / (1024 * 1024)

            print(f"✅ {num} Size Found: {size_bytes} bytes ({size_mb:.2f} MB)")
        else:
            print(f"⚠️ {num} Content-Length not found")
    else:
        print(f"❌ {num} Error: {result.stderr}")

if __name__ ==  "__main__":
    
    count = 0
    with open("TamilDigitalLibrary-Book-Details - Books.csv", "r", encoding="utf-8") as file:
        for line in file:
            book_datas = list(line.strip().split(","))
            book_name = book_datas[1]
            book_download_link = book_datas[-1]
            if book_download_link.startswith("https://tamildigitallibrary.in/"):
                count += 1
                download_books(book_name, book_download_link, count)
                chacking_size(book_download_link,count)
                break
    print()
    print("All Book Size: ", all_book_bytes)
    print("Total Size: ", sum(all_book_bytes))