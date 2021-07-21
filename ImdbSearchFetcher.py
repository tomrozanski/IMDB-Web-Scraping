import requests as requests
from bs4 import BeautifulSoup
import re

class ImdbSearchFetcher(object):

    def filtering_movies(self, movie_name):

        url = f'https://www.imdb.com/find?q={movie_name}&s=tt&ttype=ft'
        movies_dic = dict()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        movies = soup.select('td.result_text a')  # getting all movies without filtering
        links = [a.attrs.get('href') for a in
                 soup.select('td.result_text a')]  # getting all links for all of the movies

        # filtering the movies that contain the searched word and check if not "in development"
        for index in range(0, len(movies)):
            movie_string = movies[index].get_text()
            if re.match(r".*" + re.escape(movie_name), movie_string, re.IGNORECASE):
                if "(in development)" not in movie_string:
                    movie = (' '.join(movie_string.split()).replace('.', ''))
                    movies_dic[movie] = links[index]

        return movies_dic
