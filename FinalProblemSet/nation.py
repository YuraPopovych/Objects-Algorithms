
class Nation:
    def __init__(self, short_name, long_name, iso_code, iso_short, iso_long, capital):
        self.short_name = short_name
        self.long_name = long_name
        self.iso_code = iso_code
        self.iso_short = iso_short
        self.iso_long = iso_long
        self.capital = capital

def to_dictionaries(nation_list):
    nation_dictionary = {}
    for nation in nation_list:
        nation_dictionary[nation.short_name] = {
                                                "long_name": nation.long_name,
                                                "iso_code": nation.iso_code ,
                                                "iso_short": nation.iso_short,
                                                "iso_long": nation.iso_long ,
                                                "capital": nation.capital
                                                }
    return nation_dictionary



new_nation_1 = Nation("Albania", "Republic of Albania", 8, "AL", "ALB", "Tirana")
new_nation_2 = Nation("Angola", "Republic of Angola", 24, "AO", "AGO", "Luanda")
nation_list = [new_nation_1, new_nation_2]
print(to_dictionaries(nation_list))




