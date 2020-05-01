class Country():

    def __init__(self):
        self.__name = ""
        self.__starsClothes = ""
        self.__starsFood = ""
        self.__starsTourism = ""
        self.__cost = 0
        self.__coordinates = ()
    # Costructor sin parametros

    def __init__(self, name, sClothes, sFood, sTourism, cost, coor):
        self.__name = name
        self.__starsClothes = sClothes
        self.__starsClothes += " estrellas"
        self.__starsFood = sFood
        self.__starsFood += " estrellas"
        self.__starsTourism = sTourism
        self.__starsTourism += " estrellas"
        self.__cost = cost
        self.__coordinates = coor
    #Constructor con parametros

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

    def getStarsClothes(self):
        return self.__starsClothes
    def setStarsClothes(self, stars):
        self.__starsClothes = stars
        self.__starsClothes += " estrellas"

    def getStarsFood(self):
        return self.__starsFood
    def setStarsFood(self, stars):
        self.__starsFood = stars
        self.__starsFood += " estrellas"

    def getStarsTourism(self):
        return self.__starsTourism
    def setStarsTourism(self, stars):
        self.__starsTourism = stars
        self.__starsTourism += " estrellas"

    def getCost(self):
        return self.__cost
    def setCost(self, cost):
        self.__cost = cost

    def getCoordinates(self):
        return self.__coordinates
    def setCoordiantes(self, coor):
        self.__coordinates = coor