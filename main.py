from ImdbSearchFetcher import ImdbSearchFetcher
from MovieScraper import MovieScraper
from MovieFileWriter import MovieFileWriter


if __name__ == '__main__':

    fetcher = ImdbSearchFetcher()
    scraper = MovieScraper()
    file_writer = MovieFileWriter()

    search_terms = input("What movie do you want to know about?\n> ")
    filtered_movies = fetcher.filtering_movies(search_terms)
    scraped_movies = scraper.scrape(filtered_movies)
    file_writer.write_to_file(scraped_movies)
