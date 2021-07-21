import os
class MovieFileWriter(object):

    def write_to_file(self, movies, path):
        save_path = path
        file_name = "movies_file.txt"
        final_path = os.path.join(save_path, file_name)
        text_file = open(final_path, "w")

        for movie in movies:
            text_file.write(str(movie))
        print("The movie text file is in: "+path)
        text_file.close()
