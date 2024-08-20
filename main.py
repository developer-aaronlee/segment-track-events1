import csv
import json
import requests

url = 'https://api.segment.io/v1/track'
API_KEY = 'Basic api_key'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('batch_test_6.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        if len(row)==0:
           continue
        temp = row[0].split(",")

        dic = {}

        if temp[0] == "userId":
            continue

        if temp[2] != "":
            dic["equipment"] = temp[2].split("|")
        if temp[3] != "":
            dic["length"] = int(temp[3])
        if temp[4] != "":
            dic["workout_category"] = temp[4]

        new = {
                "userId": temp[0],
                "event": temp[1],
                "properties": dic,
                "timestamp": temp[5]
            }

        body = json.dumps(new)
        print(body)
        response = requests.post(url, data=body, headers=headers)
        print(response)

        # dic = {}
        #
        # if temp[0] == "userId":
        #     continue
        #
        # if temp[2] != "":
        #     dic["equipment"] = temp[2].split("|")
        # if temp[3] != "":
        #     dic["length"] = int(temp[3])
        # if temp[4] != "":
        #     dic["workout_category"] = temp[4]
        #
        # new = {
        #         "userId": temp[0],
        #         "event": temp[1],
        #         "properties": dic,
        #         "timestamp": temp[5]
        #     }
