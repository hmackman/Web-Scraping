#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..\..\..\..\Module-12 Web Scraping'))
	print(os.getcwd())
except:
	pass

#%%
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd


#%%
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


#%%
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


#%%
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
# Retrieve all elements that contain book information
articles = soup.select_one("ul.item_list li.slide")
print(articles)


#%%



#%%
# Iterate through each book
for article in articles:
    # Use Beautiful Soup's find() method to navigate and retrieve attributes
    step_one = article.find('div', class_="content_title")
    link = step_one.find('a')
    step_two = article.find('div', class_="article_teaser_body")
    body = step_two.find


#%%
news_title = (link.text)
print(news_title)


#%%
news_paragraph = (step_two.text)
print(news_paragraph)


#%%



#%%
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


#%%
url_one = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_one)


#%%
button = browser.find_by_id("full_image")
button.click()

browser = Browser("chrome", headless=False)
url_two = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_two)


#%%
url_base = "https://www.jpl.nasa.gov"


#%%
html_two = browser.html
soup_two = bs(html_two, "html.parser")


#%%
button_one = soup_two.find('a', class_='button fancybox')
button_one


#%%
url_image = soup_two.find('a', {'id':'full_image','data-fancybox-href':True}).get('data-fancybox-href')
url_image


#%%
complete_url = url_base + url_image
print(complete_url)


#%%
browser = Browser("chrome", headless=False)
url_twitter = "https://www.twitter.com/marswxreport?lang=en"
browser.visit(url_twitter)


#%%
html_three = browser.html
soup_three = bs(html_three, "html.parser")


#%%
tweet = soup_three.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


#%%
mars_weather = tweet.text.strip()
mars_weather


#%%
url_fat = "https://space-facts.com/mars/"
table_top = pd.read_html(url_fat)
table_top


#%%
data_df = table_top[0]
data_df.head()


#%%
print(data_df.to_html())


#%%
broswer = Browser('chrome', headless=False)
url_four = "https://astrogeology.usgs.gov/search/results/?q=hemisphere+enhanced&k1=target&v1=Mars"
broswer.visit(url_four)


#%%
html_four = browser.html
soup_four = bs(html_four,'html.parser')


#%%
astro_url_one = "https://astropedia.astrogeology.usgs.gov/download/Mars/Vikings/cerberus_enhanced.tif/full.jpg"
astro_url_two = "https://astropedia.astrogeology.usgs.gov/download/Mars/Vikings/schiaparelli_enhanced.tif/full/jpg"
astro_url_three = "https://astropedia.astrogeology.usgs.gov/download/Mars/Vikings/syrtis_major_enhanced.tif/full.jpg"
astro_url_four = "https://astropedia.astrogeology.usgs.gov/download/Mars/Vikings/valles_marineris_enhanced.tif/full.jpg"


#%%
astro_links = [astro_url_one, astro_url_two, astro_url_three, astro_url_four]


#%%
astro = soup_four.find_all('h3')
astro


#%%
astro_descripts = [h3.text.strip() for h3 in astro]
astro_descripts


#%%
hemisphere_pics_urls = [{'title': astro_descript, 'img_url':astro_link} for astro_descript, astro_link in zip(astro_descripts, astro_links)]
hemisphere_pics_urls


#%%



