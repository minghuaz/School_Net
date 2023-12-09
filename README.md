# School_Net
This is the final proj for building a school network to get a minimal  connection number

## Project Overview
This project is dedicated to collecting and processing information from the Google Scholar personal pages of scholars from the University of Michigan (UMICH). We automate the collection of UMICH scholar personal page links and extract information about their published papers and co-authors.

## Directory Structure
- `cache/`: Contains cached HTML content of UMICH scholars' personal pages from Google Scholar. Due to network interruptions and file upload limits, it currently includes about 100 HTML files as examples. The local cache theoretically could contain the Google Scholar pages of all UMICH scholars.
- `scholar_url_collect.py`: Collects personal page links of scholars belonging to UMICH from Google Scholar and stores them in `profiles_citation_link.csv`.
- `scholar_info_generator.py`: Visits each scholar's page in `profiles_citation_link.csv`, extracts information about their published papers and co-authors, and stores it in TXT format in `scholar_publication.txt`.

## Usage Guide
1. Ensure Python environment is installed.
2. Run `scholar_url_collect.py` to collect scholar page links.
3. Run `scholar_info_generator.py` to extract information from these pages.

## Notes
- Due to network speed and file upload restrictions, the contents of the `cache` folder are incomplete and only serve as an example for processing.
- We are still exploring how to synchronize local files directly with git.
- Please comply with the terms of use of Google Scholar and use scraping scripts responsibly.

## Contributions
Contributions of any kind are welcome! If you have any suggestions or want to improve this project, please submit a Pull Request or open an Issue.
