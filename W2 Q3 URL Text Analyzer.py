import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# URL input
url = input("Enter URL: ")

# Add browser header (IMPORTANT)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Fetch webpage
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract text
text = soup.get_text()

# Clean and split words
words = re.findall(r'\b[a-z]+\b', text.lower())

# Count frequency
word_count = Counter(words)

# Results
print("\nTotal Words:", len(words))
print("Unique Words:", len(word_count))

print("\nTop 5 Words:")
for word, count in word_count.most_common(5):
    print(word, ":", count)