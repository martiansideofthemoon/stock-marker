#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

# Downloading webpage having BSE data
res = requests.get('http://www.moneycontrol.com/india/stockpricequote/computers-software-training/careerpoint/CPI05')
res.raise_for_status()

# parsing webpage
webpage = BeautifulSoup(res.text, "lxml")
bse_span = webpage.select('#Bse_Prc_tick')[0]
bse_value = bse_span.getText().strip()

print bse_value
