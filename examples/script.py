import requests
import json

url = "https://transport.integration.sl.se/v1/sites/1002/departures?transport=METRO&line=14&forecast=60"

req = requests.get(url)
req_json = req.json()

# Steg 1: skriv ner svaret till en fil för att undersöka fälten som returneras
# with open("request.json", "w") as f:
#     json.dump(req_json, f, indent=2)

# Steg 2: skriv ut i terminal
# Upptäcker att jag får båda riktingar
# for i in range(0, len(req_json["departures"])):
#     print(req_json["departures"][i]["destination"], req_json["departures"][i]["display"])

# Steg 3: skriv ut i terminal
# Förfining av utskrift som också filterar på riktning 
for i in range(0, len(req_json["departures"])):
    if req_json["departures"][i]["direction_code"] == 2: # hårdkodad direction_code == 2
        print(req_json["departures"][i]["destination"], req_json["departures"][i]["display"])
