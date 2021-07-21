from ImdbSearchFetcher import ImdbSearchFetcher
from MovieScraper import MovieScraper
from MovieFileWriter import MovieFileWriter
import argparse

parser = argparse.ArgumentParser(description="tool that can execute queries for movie titles using imdb web site")
parser.add_argument('-m', '--movie_title', type=str, metavar="", required=True, help='Name of the movie')
parser.add_argument('-p', '--file_path', type=str, metavar="", required=True, help='Path of the file')
args = parser.parse_args()


def scrape_movie(search):
    fetcher = ImdbSearchFetcher()
    scraper = MovieScraper()

    filtered_movies = fetcher.filtering_movies(search)
    scraped_movies = scraper.scrape(filtered_movies)
    return scraped_movies


def write_to_file(movies_to_write, path):
    file_writer = MovieFileWriter()
    file_writer.write_to_file(movies_to_write, path)


if __name__ == '__main__':
    movies = scrape_movie(args.movie_title)
    write_to_file(movies, args.file_path)
    print("The scraping was done successfully")
