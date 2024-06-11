import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time
import re
import pandas as pd

def split_price(price):
    match = re.match(r'([^\d]+)?([\d,.]+)', price.strip())
    if match:
        currency = match.group(1).strip() if match.group(1) else ''
        amount = match.group(2).strip() if match.group(2) else ''
        return currency, amount
    return '', ''

def scrape_freelancer_jobs(pages_to_scrape):
    base_url = 'https://www.freelancer.com/jobs/'
    current_page = 1
    total_projects = 0

    with open('projects.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Status', 'Description', 'Tags', 'Currency', 'Price', 'Proposals', 'Location', 'Payment Method']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            url = f'{base_url}?page={current_page}'
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            projects = soup.find_all(class_='JobSearchCard-item')
            if not projects:
                break
            
            total_projects += len(projects)

            with tqdm(total=len(projects), desc=f"Page {current_page} Progress") as pbar:
                for project in projects:
                    try:
                        title = project.find(class_='JobSearchCard-primary-heading-link').text.strip()
                        detail_url_suffix = project.find(class_='JobSearchCard-primary-heading-link')['href']
                        detail_url = f'https://www.freelancer.com{detail_url_suffix}'
                        detail_response = requests.get(detail_url)
                        detail_response.raise_for_status()
                        detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
                    except AttributeError:
                        title = "N/A"
                        detail_soup = None
                    except requests.exceptions.HTTPError as e:
                        print(f"Failed to retrieve {detail_url}: {e}")
                        detail_soup = None
                    
                    status = project.find(class_='JobSearchCard-primary-heading-status Tooltip--top').text.strip() if project.find(class_='JobSearchCard-primary-heading-status Tooltip--top') else "N/A"
                    description = project.find(class_='JobSearchCard-primary-description').text.strip() if project.find(class_='JobSearchCard-primary-description') else "N/A"
                    tags = project.find(class_='JobSearchCard-primary-tagsLink').text.strip() if project.find(class_='JobSearchCard-primary-tagsLink') else "N/A"
                    proposals = project.find(class_='JobSearchCard-secondary-entry').text.strip() if project.find(class_='JobSearchCard-secondary-entry') else "N/A"

                    if detail_soup:
                        try:
                            price = detail_soup.find('h2', class_='ng-star-inserted').text.strip()
                            currency, amount = split_price(price)
                        except AttributeError:
                            currency, amount = "N/A", "N/A"
                        
                        try:
                            location_container = detail_soup.find(class_='FlexContainer')
                            location = location_container.find('div', class_='NativeElement').text.strip()
                        except AttributeError:
                            location = "N/A"
                        
                        try:
                            payment_method = detail_soup.find('div', {'role': 'paragraph', 'class': 'NativeElement ng-star-inserted', 'data-color': 'foreground'}).text.strip()
                        except AttributeError:
                            payment_method = "N/A"
                    else:
                        currency, amount = "N/A", "N/A"
                        location = "N/A"
                        payment_method = "N/A"

                    writer.writerow({
                        'Title': title, 
                        'Status': status, 
                        'Description': description, 
                        'Tags': tags, 
                        'Currency': currency, 
                        'Price': amount, 
                        'Proposals': proposals, 
                        'Location': location,
                        'Payment Method': payment_method
                    })
                    pbar.update(1)
            
            current_page += 1
            if pages_to_scrape != 0 and current_page > pages_to_scrape:
                break

            time.sleep(1)

    # Konversi data dari CSV ke Excel setelah selesai scraping
    df = pd.read_csv('projects.csv')
    output = 'output.xlsx'
    df.to_excel(output, index=False)

 # Ganti angka di dalam fungsi dengan jumlah halaman yang ingin Anda scrape


