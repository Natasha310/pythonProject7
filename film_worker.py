import os


class Film:
    url_trailer = "https: // www.imdb.com / video / vi3722091801 /"
    title = "Crazy, Stupid, Love."
    description = "A middle-aged husband's life changes dramatically when his wife asks him for a divorce.\
                       He seeks to rediscover his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars."
    director_writer = ['Glenn Ficarra', 'John Requa', 'Dan Fogelman']
    cast = ['Steve Carell', 'Ryan Gosling', 'Julianne Moore']
    run_time = int
    imdb_rate = float
    year = int
    budget = int
    profit = True
    oscar = False
    storage_address = None

    def __int__(self, year, imdb_rate):
        self.year = 2011
        self.imdb_rate = imdb_rate

    def upload_file(self):
        os.chdir('film_storage')
        films = os.listdir()
        test_url = " "
        for film in films:
            print(film)
            if film in test_url:
                open(test_url.txt, 'w')
            continue
            os.chdir('../')

    def get_film_address(self):
        os.chdir('C:\Users\nataliian\PycharmProjects\pythonProject6\film_player\film_storage')
        files = os.getcwd()
        return files
    def run_t(self):
        run_time = 118
        if run_time == int:
            print("minutes")

    def budget_(self):
        budget = 50
        if budget == int:
            print("$" + budget + "million")

    def profitable(self):
        profit = True
        if profit:
            print("Yes")
        else:
            print("No")

    def oscar_nom(self):
        profit = False
        if profit:
            print("Yes")
        else:
            print("No")