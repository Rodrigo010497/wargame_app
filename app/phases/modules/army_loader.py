from bs4 import BeautifulSoup
import json
import os
from prettytable import PrettyTable as pt

class unit():
    def __init__(self, name ):
        self.name = name
        self.get_info()
        # if len(list(self.melee_options.items())) > 0:
        self.equiped_melee = list(self.melee_options.items())[0]
        # if len(list(self.ranged_options.items())) > 0:
        self.equiped_ranged = list(self.ranged_options.items())[0]
        self.categorize_skills()

    def get_info(self):
        mopdule_path = os.path.dirname(__file__)
        self.file_path = os.path.join(mopdule_path, '../data/Imperium-GreyKnights.xml')
        with open(self.file_path, 'r') as f:
            data = f.read()
        xml_data = BeautifulSoup(data, "xml")

        troop = xml_data.find('selectionEntry', {'name': self.name})
        self.stats = {}
        self.abilities = {}
        self.ranged_options = {}
        self.melee_options = {}

        for i in troop.find_all('profile', {"typeName": "Unit"}):
            self.stats = {x['name']: " ".join(x.contents) for x in i.find_all('characteristic')}

        for i in troop.find_all('profile', {"typeName": "Abilities"}):
            skill = i.find_all("characteristic", {"name": "Description"})[0].contents[0]
            self.abilities[i['name']] = skill

        for x in troop.find_all('profile', {"typeName": "Melee Weapons"}):
            self.melee_options[x["name"]] = {i['name']: " ".join(i.contents) for i in x.find_all('characteristic')}

        for x in  troop.find_all('profile', {"typeName": "Ranged Weapons"}):
            self.ranged_options[x["name"]] = {i['name'] : " ".join(i.contents) for i in x.find_all('characteristic')}



    def pick_melee_weapon(self, choice):
        self.equiped_melee = self.melee_options[choice]
    def pick_ranged_weapon(self, choice):
        self.equiped_ranged = self.ranged_options[choice]

    def categorize_skills(self):
        print(self.abilities)
        for p, x in self.abilities.items():
            if "move" in x:
                self.movement_abilities[p] = x
            if "charge" in x:
                self.charge_abilities[p] = x


    def format(self, table, title = None):
        tb = pt()
        tb.title = title
        tb.field_names = list(table.keys())
        tb.add_row(list(table.values()))
        return tb

    def display_move_phase(self):
        print(self.stats["M"])

    def display_shooting_phase(self):
        print(self.equiped_ranged)

    def get_all_army_units(self):
        with open(self.file_path, 'r') as f:
            data = f.read()
        xml_data = BeautifulSoup(data, "xml")

        troop = xml_data.find_all('profile', {"typeName": "Unit"})

        return [i['name'] for i in troop]

    def display_fighting_phase(self):
        print(self.equiped_melee)


    
    def phase_filter(self, phase):
        print(self.format(self.stats, self.name))
        filter = {
            'command': "",
            'movement': self.display_move_phase(),
            'shooting': self.format(self.equiped_ranged[1],self.equiped_ranged[0]),
            'charge': "",
            'fight': ""
        }
        print(filter[phase])



# Reading the data inside the xml
# file to a variable under the name
# data


# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object


# Finding all instances of tag
# `unique`
# with open('Imperium-GreyKnights.xml', 'r') as f:
#     data = f.read()
# Bs_data = BeautifulSoup(data, "xml")
# b_unique = Bs_data.find_all('profiles')
#
# # print(b_unique)
#
# # Using find() to extract attributes
# # of the first instance of the tag
# b_name = Bs_data.find('selectionEntry', {'name': 'Brother-Captain'})
#
# # print(b_name)
# print('============')
#
# stats = {}
# for i in b_name.find_all('profile', {"typeName" : "Unit"}):
#     print("======")
#     stats = {x['name'] : " ".join(x.contents) for x in i.find_all('characteristic')}
#     print(stats)
#
# skills = {}
# for i in b_name.find_all('profile', {"typeName" : "Abilities"}):
#     skill = i.find_all("characteristic", {"name": "Description"})[0].contents[0]
#     print(skill)
#     skills[i['name']] = skill
# print(skills)
#
# entry = b_name.find_all('selectionEntry')
#
#
# melee_options = b_name.find_all('profile',{"typeName": "Melee Weapons"})
# ranged_options = b_name.find_all('profile',{"typeName": "Ranged Weapons"})
# # print(ranged_options)
#
# for x in melee_options:
#     print(x["name"])
#     melee = {i['name']: " ".join(i.contents) for i in x.find_all('characteristic')}
#     print(melee)
#
# ranged = {}
# for x in ranged_options:
#     ranged[x["name"]] = {i['name'] : " ".join(i.contents) for i in x.find_all('characteristic')}
# print(ranged)


#
# for x in units:
#     unit(x).phase_filter('shooting')
# unit('Brother-Captain')
# for i in army:
#     i.display_all()
#     print("+++++++++++++++++++++++++++++++++")




# with open('../data/Imperium-GreyKnights.xml', 'r') as f:
#     data = f.read()
# xml_data = BeautifulSoup(data, "xml")
#
# troop = xml_data.find_all('profile',{"typeName" : "Unit"})
#
# units = [i['name'] for i in troop]
#
# for i in units:
#     q = unit(i)
#     for p, x in q.abilities.items():
#         if "move" in x:
#             print(x)
#             print("~~~~~~~~~")