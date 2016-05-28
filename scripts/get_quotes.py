#!/usr/bin/env python

from mechanize import Browser
from bs4 import BeautifulSoup as bs

# set up mechanize header
headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')]

# define target URL
url = "http://www.bseindia.com/getquote.htm"

br = Browser()

# browser parameters
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False) 

br.addheaders = headers

# make request
main_page = br.open(url)

# select the default form
br.select_form(nr=0)
br.find_control(id="suggestBoxEQ").value = "CAREERP"

# submit form
br.submit()
page_response = bs(br.response().read())

quote = page_response.find_all('div',{'class':'newsrheadingdiv'})
print quote
