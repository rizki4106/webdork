from module import module
import os, hashlib, requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup

remove .google-cookie
try:
    os.remove('.google-cookie')
except:
    pass

module.start()