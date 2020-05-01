class User():
    def __init__(self):
        self.__name = ""
        self.__capital = 0
        self.__countryOrigin = ""
        self.__countryDestiny = ""
        self.__tasteForFood = ""
        self.__tasteForTourism = ""
        self.__tasteForClothes = ""
    #Costructor sin parametros

    def __init(self, name, capital, countryO, countryD, sFood, sTourism, sClothes):
        self.__name = name
        self.__capital = capital
        self.__countryOrigin = countryO
        self.__countryDestiny = countryD
        self.__tasteForFood = sFood
        self.__tasteForFood += " estrellas"
        self.__tasteForTourism = sTourism
        self.__tasteForTourism += " estrellas"
        self.__tasteForClothes = sClothes
        self.__tasteForClothes += " estrellas"
    #Constructor con parametros

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

    def getCapital(self):
        return  self.__capital
    def setCapital(self, cap):
        self.__capital = cap

    def getCountryOrigin(self):
        return self.__countryOrigin
    def setCountryOrigin(self, country):
        self.__countryOrigin = country

    def getCountryDestiny(self):
        return self.__countryDestiny
    def setCountryDestiny(self, country):
        self.__countryDestiny = country

    def getTasteFood(self):
        return self.__tasteForFood
    def setTasteFood(self, stars):
        self.__tasteForFood = stars
        self.__tasteForFood += " estrellas"

    def getTasteClothes(self):
        return self.__tasteForClothes
    def setTasteClothes(self, stars):
        self.__tasteForClothes = stars
        self.__tasteForClothes += " estrellas"

    def getTasteTourism(self):
        return self.__tasteForTourism
    def setTasteTourism(self, stars):
        self.__tasteForTourism = stars
        self.__tasteForTourism += " estrellas"