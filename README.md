# School_Net
This is the final project for building a school network to obtain a minimal connection number, akin to the "Kevin Bacon" number within the academic context of the University of Michigan (UMICH).

## Project Overview
The project automates the collection of UMich scholar personal page links from Google Scholar and extracts information about their published papers and co-authors. The objective is to compute the academic "Kevin Bacon" number, which represents the degrees of separation between scholars within the UMich community.

## Directory Structure
- `cache/`: Contains cached HTML content of UMich scholars' personal pages from Google Scholar. This is a partial collection due to network interruptions and file upload limits, showcasing about 100 HTML files as examples.
- `scholar_url_collect.py`: Script to collect personal page links of scholars belonging to UMich from Google Scholar and store them in `profiles_citation_link.csv`.
- `scholar_info_generator.py`: Script to visit each scholar's page in `profiles_citation_link.csv`, extract information about their published papers and co-authors, and store it in TXT format in `scholar_publication.txt`.
- `Bacon_mihzhang.py`: The script for calculating the academic "Kevin Bacon" number in four different scenarios as described in the project functionalities.

## Usage Guide
1. Ensure the Python environment is properly set up with all necessary packages installed.
2. Execute `scholar_url_collect.py` to gather scholar page links.
3. Run `scholar_info_generator.py` to pull information from these scholar pages.
4. Modify the `main()` function in `Bacon_mihzhang.py` to set the path for `scholar_publications.txt`. If it's located in the same directory as `Bacon_mihzhang.py`, no changes are required.
5. Use `Bacon_mihzhang.py` to compute the academic "Kevin Bacon" numbers based on the extracted data.

## Required Packages
Ensure the following Python packages are installed:
- `requests`
- `beautifulsoup4 (bs4)`
- `urllib`
- `csv`
- `time`
- `selenium`

These can be installed using the command: `pip install requests beautifulsoup4 urllib3 csv time selenium`

## Notes
- The `cache` folder's content is not comprehensive and is provided as a processing example due to network and upload constraints.
- Efforts are ongoing to synchronize local files directly with git.
- Please adhere to the Google Scholar terms of use and utilize scraping scripts responsibly.

## Contributions
Contributions are welcome! If you have suggestions or improvements for this project, please submit a Pull Request or open an Issue on GitHub.
