
#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!
class Burrito:
    
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False ):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
   
    def set_meat(self, meat):
        if type(meat) == str:
            meat = meat.lower()
        valid_options = ["chicken", "pork", "steak", "tofu"]
        if meat in valid_options or type(meat) == bool:
            self.meat = meat
        else:
            self.meat = False            
    def get_meat(self):
        return self.meat
    
    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False
    def get_to_go(self):
        return self.to_go

    def set_rice(self, rice):
        if type(rice) == str:
            rice = rice.lower()
        valid_options = ["brown", "white"]
        if rice in valid_options or type(rice) == bool:
            self.rice = rice
        else:
            self.rice = False
    def get_rice(self):
        return self.rice

    def set_beans(self, beans):
        if type(beans) == str:
            beans = beans.lower()
        valid_options = ["black", "pinto"]
        if beans in valid_options or type(beans) == bool:
            self.beans = beans
        else:
            self.beans = False
    def get_beans(self):
        return self.beans
    
    def set_extra_meat(self, extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False
    def get_extra_meat(self):
        return self.extra_meat

    def set_guacamole(self, guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
        else:
            self.guacamole = False
    def get_guacamole(self):
        return self.guacamole

    def set_cheese(self, cheese):
        if type(cheese) == bool:
            self.cheese = cheese
        else:
            self.cheese = False
    def get_cheese(self):
        return self.cheese

    def set_pico(self, pico):
        if type(pico) == bool:
            self.pico = pico
        else:
            self.pico = False
    def get_pico(self):
        return self.pico

    def set_corn(self, corn):
        if type(corn) == bool:
            self.corn = corn
        else:
            self.corn = False
    def get_corn(self):
        return self.corn
      

newBurrito = Burrito("Tofu", True, True, True)
print(newBurrito.meat)
print(newBurrito.get_meat())
print(newBurrito.to_go)
print(newBurrito.guacamole)
print(newBurrito.get_beans())




