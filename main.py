import re
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

# Initiate a session and get the page content
session_object = requests.Session()
r = session_object.get('https://www.cricbuzz.com/cricket-match/live-scores/recent-matches')
soup = bs(r.content, 'html5lib')

# Locate the scores section
Scores = soup.find('div', attrs={"class": "cb-col cb-col-100 cb-rank-tabs"})

# Function to extract match number from URL
def extract_number(url):
    match = re.search(r'/live-cricket-scores/(\d+)/', url)
    return match.group(1) if match else None

# Initialize match list and dictionary
matchlist = []
matchdict = {}

# Extract match numbers and current timestamp
for row in Scores.findAll("a", class_="cb-lv-scrs-well cb-lv-scrs-well-complete"):
    match_number = extract_number(row.get('href'))
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    matchlist.append([match_number, timestamp])

# Print the match list
# print(matchlist)

# # Function to append list to file
def append_list_to_file(lst, file):
    with open(file, 'a') as f:
        # Convert list to string and write to file
        for item in lst:
            f.write(str(item) + '\n')

# # File name to write the data
file_name = 'match_list.txt'

# # Append the match list to the file
append_list_to_file(matchlist, file_name)
