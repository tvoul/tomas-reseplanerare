import requests

def get_departures(line, direction):

    url = f"https://transport.integration.sl.se/v1/sites/1002/departures?transport=METRO&line={line}&forecast=60"

    req = requests.get(url)
    req_json = req.json()

    departures = []

    for i in range(0, len(req_json["departures"])):

        if req_json["departures"][i]["direction_code"] == int(direction):

            departures.append({
                "destination": req_json["departures"][i]["destination"],
                "display": req_json["departures"][i]["display"]
            })

    return departures
