import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

url_parent = 'https://www.rbauction.com/2012-CATERPILLAR--HYDRAULIC-EXCAVATORHEX?invId=9900235&id=ar&auction=EDMONTON-AB-2017103'
response = requests.post(url_parent)
soup = BeautifulSoup(response.content, 'html.parser')
