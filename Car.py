class Car:

    def __init__(self, url, brand, name, price, fuel, km, year):
        self.set_url(url)
        self.set_brand(brand)
        self.set_name(name)
        self.set_price(price)
        self.set_fuel(fuel)
        self.set_km(km)
        self.set_year(year)

    def set_url(self, url):
        self.url = url

    def set_brand(self, brand):
        self.brand = brand

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_fuel(self, fuel):
        self.fuel = fuel

    def set_km(self, km):
        self.km = km

    def set_year(self, year):
        self.year = year

    def get_url(self):
        return self.url

    def get_brand(self):
        return self.brand

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_fuel(self):
        return self.fuel

    def get_km(self):
        return self.km

    def get_year(self):
        return self.year

        