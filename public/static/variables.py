import json
list_names = []
list_second_names = []

with open("Console\Generate_Data\public\json\data.json", 'r', encoding='utf-8') as content:
    data = json.load(content)
    list_names = data["first_names"]
    list_second_names = data["names_de-sh"]


# json = open("Console\Generate_Data\public\json\data.json", "+rb")
# list_names = json["first_names"]
# list_second_names = json["names_de-sh"]
# print("Nombres: ", list_names)
# print("Apellidos: ", list_second_names)