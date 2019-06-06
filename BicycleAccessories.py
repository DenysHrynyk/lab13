class BicycleAccessories:

    def __init__(self, name, weight, manufacturer, producing_country, types_manufacturer):
        self.name = name
        self.weight = weight
        self.manufacturer = manufacturer
        self.producing_country = producing_country
        self.types_manufacturer = types_manufacturer

    def __str__(self):
        return "\nName:  " + str(self.name)\
                + "\nWeight:  " + str(self.weight)\
                + "\nManufacturer:  " + str(self.manufacturer)\
                + "\nProducing country:  " + str(self.producing_country)\
                + "\nTypes Manufacturer:  " + str(self.types_manufacturer)

    def __del__(self):
        print("Removed: " + self.name)
