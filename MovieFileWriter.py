class MovieFileWriter(object):

    def write_to_file(self, movies):
        text_file = open("movies_file.txt", "w")

        for movie in movies:
            text_file.write(str(movie))

        text_file.close()
