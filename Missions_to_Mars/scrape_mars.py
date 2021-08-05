
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os


def scrape_info():
	executable_path = {"executable_path": ChromeDriverManager().install()}
	browser = Browser("chrome", **executable_path, headless=False)



	url = "https://redplanetscience.com/"
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")



	mars = {}


	results = soup.find_all('div', attrs={'id': 'news', 'class': 'container'})

	for result in results:
		try:
			headline=result.find('div', attrs={'content_title'}).text
			content= result.find('div', attrs={'article_teaser_body'}).text
			if (headline and content):
				print(headline)
				print(content)
				mars = {
					'headlines': headline,
					'content': content
				}
		except Exception as e:
			print(e)	



	url2="https://spaceimages-mars.com/"
	browser.visit(url2)



	featured_image_url = browser.links.find_by_partial_text("image/featured/mars3.jpg")
	featured_image_url = url2 + featured_image_url
	featured_image_url
	mars['featured_image_url'] = featured_image_url



	url3="https://galaxyfacts-mars.com/"
	browser.visit(url3)



	mars_table = pd.read_html(url3)
	mars_table=mars_table[0].to_html()
	mars_table
	mars['mars_facts']=mars_table


	url4 = "https://marshemispheres.com/"
	browser.visit(url4)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')



	results = soup.find('div', class_='description')
	results



	url4 = "https://marshemispheres.com/"
	browser.visit(url4)

	hemisphere_image_urls = []
	results = browser.find_by_css('a.product-item img')
	for result in range(len(results)):
		hemispheres= {}
		browser.find_by_css('a.product-item img')[result].click()
		image = browser.links.find_by_text('Sample').first
		hemispheres['image_url']=image['href']
		hemispheres['title']= browser.find_by_css('h2.title').text
		hemisphere_image_urls.append(hemispheres)
		browser.back()

	mars['hemisphere_image_urls'] = hemisphere_image_urls

	return mars
if __name__=='__main__':
	print(scrape_info())


