import requests as requests
from bs4 import BeautifulSoup
from Movie import Movie


class MovieScraper(object):

    def scrape(self, movies_dic):
        base_url = 'https://www.imdb.com'
        movies = []
        for item in movies_dic.items():
            new_url = base_url + ''.join(item[1])
            response = requests.get(new_url)
            soup = BeautifulSoup(response.text, 'lxml')

            # getting list of genres
            genres = soup.select('a.GenresAndPlot__GenreChip-cum89p-3.fzmeux.ipc-chip.ipc-chip--on-baseAlt span')
            movie_genres = [movie.get_text() for movie in genres]

            # getting the MPAA of the movie, not all of the movies has it
            rating = soup.select(
                'a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color.TitleBlockMetaData__StyledTextLink-sc-12ein40-1.rgaOW')
            if len(rating) > 1:
                movie_rating = rating[1].get_text()
            else:
                movie_rating = ""

            # find the duration of the movie
            '''
           the duration of the movie is the last li so we need to check every movie how mush detils we have to know the place
           of the duration in the ul

            '''
            ul_tag = soup.find('ul', {
                'class': 'ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt'})
            li_tag = ul_tag.find_all('li')
            if len(li_tag) < 2:
                movie_duration = ""
            else:
                movie_duration = li_tag[-1].get_text()

            temp = soup.select(
                'div.Hero__ContentContainer-kvkd64-10 ul.ipc-metadata-list.ipc-metadata-list--dividers-all.title-pc-list.ipc-metadata-list--baseAlt')
            movie_directors = ""
            movie_stars = ""
            if len(temp) > 0:
                li_rows = temp[0].select(
                    'div.Hero__ContentContainer-kvkd64-10 ul.ipc-metadata-list.ipc-metadata-list--dividers-all.title-pc-list.ipc-metadata-list--baseAlt > li')
                for li in li_rows:
                    rol = li.select('li > *')[0]
                    if 'Director' in rol.get_text():
                        movie_directors = [x.get_text() for x in li.select('li')]
                    if 'Star' in rol.get_text():
                        movie_stars = [x.get_text() for x in li.select('li')]

            movie = Movie(item[0], movie_genres, movie_rating, movie_duration, movie_directors, movie_stars)
            movies.append(movie)
        return movies
