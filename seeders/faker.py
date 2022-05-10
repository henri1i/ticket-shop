import requests
import json
import random

class Faker:
    @staticmethod
    def getRandomData(count: int, filePath: str):
        file = open('/home/henri/dev/ticket-shop/seeders/'+filePath, 'r')
        fileData = json.loads(file.read())
        
        data = []
        for i in range(count):
            randomIndex = random.randint(0, len(fileData)-1)
            data.append(fileData[randomIndex])

        return data