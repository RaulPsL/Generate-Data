class CreateDataBase:
    def createDB(self, namedb):
        print(f"""
              CREATE DATABASE IF NOT EXISTS `{namedb}`;
              USE `{namedb}`;
              """)