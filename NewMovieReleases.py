from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://123-movie.cc/123movies-free-online/'
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

movie_titles = []
for title in soup.findAll('span', {'class': 'mli-info'}):
    titles =title.find('h2').get_text()
    movie_titles.append(titles)

topmovies=pd.DataFrame({
    'Movie_Title': movie_titles
})

print(topmovies)
