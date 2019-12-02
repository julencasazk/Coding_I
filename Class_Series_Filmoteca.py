class Serie():
    def __init__(self,title,seasons,genre,year):
        self.__title = title
        self.__seasons = seasons
        self.__genre = genre
        self.__year = year
        self.__genrelist = ["action", "humor", "thriller", "drama"]
    
    def getTitle(self):
        return self.__title
    
    def getSeasons(self):
        return self.__seasons
    
    def getGenre(self):
        return self.__genre
    
    def getGenreList(self):
        return self.__genrelist
    
    def getYear(self):
        return self.__year

    def setSeasons(self, seasn):
        if seasn > 0:
            self.__seasons = seasn

    def setYear(self, yr):
        if yr > 1900:
            self.__year = yr

    def setGenre(self, gen):
        if gen in self.__genrelist:
            self.__genre = gen

class GestionSeries():

    def __init__(self):
        self.__filmoteca = []
        for i in range(0,100):
            self.__filmoteca.append(Serie("i",i,"i",i))
    
    def setFilm(self, show, n):
        self.__filmoteca[n] = show
    
    def getFilmoteca(self):
        return self.__filmoteca


s1 = Serie("Holiis",5,"action",1998)
s2 = Serie("Bruh2",3,"humor",2015)
s3 = Serie("Friends",250,"drama",1915)

bruhfilm = GestionSeries()
bruhfilm.setFilm(s1,0)
bruhfilm.setFilm(s2,1)
bruhfilm.setFilm(s3,2)
print(bruhfilm.getFilmoteca())


  
