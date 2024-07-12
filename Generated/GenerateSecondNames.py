class GenerateSecondNames:
    json = open("../public/json/data.json", "+rb")
    list_second_names = []
    def createSecondNames(self):
        return self.list_second_names.append(self.json["first_names"])