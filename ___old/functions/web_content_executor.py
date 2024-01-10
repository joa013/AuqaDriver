from functions import requests
from functions import time

class WebContentExecutor:

    def __init__(self, deviceIP, deviceName, location, nameValueTable):
        self.deviceIP = deviceIP
        self.deviceName = deviceName
        self.location = location 
        self.nameValueTable = nameValueTable
    
    def execute(self):
        try:
            timestamp = round(time.time())
            print(timestamp)
            http = "http://" + self.deviceIP + self.location
            print(http)
            print(self.deviceIP)
            print(self.deviceName)
            print(self.location)
            print(self.nameValueTable)
            if self.nameValueTable != None:
                http = http + "?"
                for row in self.nameValueTable:
                    print(row)
                    http = http + row[0] + "=" + row[1]
            print(http)
            response = requests.get(http,timeout=5)


        except requests.exceptions.Timeout:
            print("cos sie zesralo")