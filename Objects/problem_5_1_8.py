


class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False ):
        self.meat = meat
        self.to_go = to_go
        self.rice = rice
        self.beans = beans
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn



newBurrito = Burrito("Tofu", True, True, True)
print(newBurrito.to_go)
print(newBurrito.guacamole)


