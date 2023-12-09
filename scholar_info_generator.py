import csv
import requests
import time  
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse, parse_qs
    
    
# def scrape_google_scholar_profile(profile_url):
#     # Initialize a list to store publication information
#     # Parse the URL
#     parsed_url = urlparse(profile_url)

#     # Use parse_qs to parse out the query parameters
#     query_params = parse_qs(parsed_url.query)

#     # Extract the user_id
#     user_id = query_params['user'][0] if 'user' in query_params else None
    
#     base_url = 'https://scholar.google.com/citations'
    
#     publication_info = []
#     cstart = 0  # start index for publications on the current page
#     pagesize = 20  # number of publications per page
    
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
#         'Accept': '*/*',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Connection': 'keep-alive'
#     }
    
#     try:
#         while True:
#             # Construct the URL for the current page of results
#             profile_url = f'{base_url}?user={user_id}&cstart={cstart}&pagesize={pagesize}'
            
#             # Send a GET request to the Google Scholar profile URL
#             response = requests.get(profile_url, headers=headers)
#             response.raise_for_status()
            
#             # Parse the HTML content of the page using BeautifulSoup
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Check if there are publications on the current page
#             publications = soup.find_all('tr', class_='gsc_a_tr')
#             if not publications or len(publications) < pagesize:
#                 # No more publications or fewer than expected, break the loop
#                 break
            
#             # Iterate through each publication entry
#             for publication in publications:
#                  # Extract the publication title
#                 title_data = publication.find('a', class_='gsc_a_at')
#                 title = title_data.text.strip() if title_data else 'No Title'
                
#                 # Extract the list of authors; multiple authors are contained within the same div
#                 author_data = publication.find('div', class_='gs_gray')
#                 authors = author_data.text.strip().split(', ') if author_data else ['No Authors']
                
#                 # Format the publication information
#                 info = f"{title}/{'/'.join(authors)}"
            
#                 # Append to the list
#                 publication_info.append(info)
                
#                 # Be polite and don't hammer the server, sleep for 1 second
#                 time.sleep(0.5)
#                 # Return the list of publication information
                
            
#             # Increment cstart to move to the next page of results
#             cstart += pagesize
            
#             # Be polite and don't hammer the server, sleep for 1 second
#             time.sleep(1)
        
#         # Return the list of publication information
#         return publication_info
#     except Exception as e:
#         print(f"Error scraping profile: {str(e)}")
#         return []
    

def scrape_google_scholar_profile(profile_url):
    # Initialize a list to store publication information
    publication_info = []
    # Parse the URL to extract the user_id
    parsed_url = urlparse(profile_url)
    query_params = parse_qs(parsed_url.query)
    user_id = query_params['user'][0] if 'user' in query_params else None
    
    base_url = 'https://scholar.google.com/citations'
    cstart = 0  # start index for publications on the current page
    pagesize = 20  # number of publications per page
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }
    
    # Define cache directory and file path
    cache_dir = 'cache'
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    cache_file_path = os.path.join(cache_dir, f'{user_id}.html')

    try:
        # Check if cache file exists
        if not os.path.isfile(cache_file_path):
            while True:
                # Construct the URL for the current page of results
                profile_url = f'{base_url}?user={user_id}&cstart={cstart}&pagesize={pagesize}'
                
                # Send a GET request to the Google Scholar profile URL
                response = requests.get(profile_url, headers=headers)
                response.raise_for_status()
                
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Check if there are publications on the current page
                publications = soup.find_all('tr', class_='gsc_a_tr')
                if not publications or len(publications) < pagesize:
                    # No more publications or fewer than expected, break the loop
                    break
                
                # Iterate through each publication entry
                for publication in publications:
                    # Extract the publication title and authors
                    title_data = publication.find('a', class_='gsc_a_at')
                    title = title_data.text.strip() if title_data else 'No Title'
                    
                    author_data = publication.find('div', class_='gs_gray')
                    authors = author_data.text.strip().split(', ') if author_data else ['No Authors']
                    
                    # Format the publication information
                    info = f"{title}/{'/'.join(authors)}"
                
                    # Append to the list
                    publication_info.append(info)
                    
                # Increment cstart to move to the next page of results
                cstart += pagesize
                
                # Be polite and don't hammer the server, sleep for 0.5 second
                time.sleep(0.5)
            
            # Cache the results by saving the last page source to a file
            with open(cache_file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
        else:
            # Load the content from the cache file
            with open(cache_file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')
                publications = soup.find_all('tr', class_='gsc_a_tr')
                for publication in publications:
                    # Extract the publication title and authors
                    title_data = publication.find('a', class_='gsc_a_at')
                    title = title_data.text.strip() if title_data else 'No Title'
                    
                    author_data = publication.find('div', class_='gs_gray')
                    authors = author_data.text.strip().split(', ') if author_data else ['No Authors']
                    
                    # Format the publication information
                    info = f"{title}/{'/'.join(authors)}"
                
                    # Append to the list
                    publication_info.append(info)
                    

        # Return the list of publication information
        return publication_info
    except Exception as e:
        print(f"Error scraping profile: {str(e)}")
        return []


if __name__ == '__main__':
    # Read the CSV file containing profile URLs
    csv_file = 'profiles_citation_link.csv'  # Replace with your CSV file path
    output_file = 'scholar_publications.txt'  # Replace with your desired output file path

    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as output:
        # Open the CSV file containing profile URLs
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Iterate through each row (profile URL)
            for row in reader:
                profile_url = row[0]
                print(f"Scraping {profile_url}...")
                
                # Scrape the profile and get publication information
                publication_info = scrape_google_scholar_profile(profile_url)
                
                # Write the publication information to the output file
                if publication_info:
                    output.write('\n'.join(publication_info) + '\n')
                    print(f"Scraped {len(publication_info)} publications from {profile_url}")

    print("Scraping complete. Data saved to publications.txt.")

# url = '/citations?hl=en&user=qdho5P0AAAAJ'
# print(scrape_google_scholar_profile(url))
