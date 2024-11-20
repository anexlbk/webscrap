import requests
from bs4 import BeautifulSoup

# URL of the page containing multiple PDF links
r = requests.get("https://droit.mjustice.dz/sites/default/files/portail/nouv_arrets_c_s_2020/")

print(r)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


## this code to get  any html and css code of anypage u want
