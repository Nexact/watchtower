from modules import hackernews 
from modules import lobsters
from modules import lapresse
from modules import radiocanada
from modules import netsec
from modules import bleepingcomputer

import json


if __name__ == "__main__":
    data = []

    hackernews_data = hackernews.get_hackernews()
    lobsters_data = lobsters.get_lobsters()
    #lapresse_data = lapresse.get_lapresse()
    #radiocanada_data = radiocanada.get_radiocanada()
    netsec_data = netsec.get_netsec()
    bleepingcomputer_data = bleepingcomputer.get_bleepingcomputer()

    # prepare json dump 
    data.append(hackernews_data)
    data.append(lobsters_data)
    #data.append(lapresse_data)
    #data.append(radiocanada_data)
    data.append(netsec_data)
    data.append(bleepingcomputer_data)

    print(json.dumps(data, indent=4))

    with open("data.json", "w") as outfile:
        outfile.write(json.dumps(data, indent=4))