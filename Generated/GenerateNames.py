from public.static import variables
import random

class GenerateNames:
    json = open("../public/json/data.json", "+rb")
    list_name = []
    def createNames(self, lot, pos):
        if pos < lot:
            self.list_name.append(variables.list_names[random.randint(1, lot)])
            return self.createNames(lot, pos+1)
        return variables.list_name

    def createNickNames(self, lot, pos):
        if pos < lot:
            self.list_names.append(variables.list_names[random.randint(1, lot)])
            return self.createNickNames(lot, pos+1)
        return variables.list_names