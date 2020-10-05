class Movie(object):
    __title = ""
    __type = ""
    __year = ""
    __plot = ""
    __poster = ""

    def __init__(self):
        print("Init empty Movie Obj")

    def __init__(self, title, type, year, plot, poster):
        print(f"Init Movie Obj with title={title}")
        self.__title = title
        self.__type = type
        self.__year = year
        self.__plot = plot
        self.__poster = poster

    # getters
    def get_title(self):
        return self.__title

    def get_type(self):
        return self.__type

    def get_year(self):
        return self.__year

    def get_plot(self):
        return self.__plot

    def get_poster(self):
        return self.__poster
