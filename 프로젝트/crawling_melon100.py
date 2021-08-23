# Import packages
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Get HTML using Webdriver with BeautifulSoup
driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Get songs top 100 within 24hour
songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')

# Make a DataFrame
list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer), columns=['Rank', 'Title', 'Singer'])
print(data.head())

# Close webdriver
driver.close()
driver.quit()

# Save a DataFrame to a Excel File(.xlsx)
now = datetime.now()
filename = now.strftime('Melon_Top100_at_%Y%m%d_%Hh%Mm.xlsx')
data.to_excel(filename, index=False)