import json
from collections import Counter

output, data_file = 'output.md', open('data/data.json')
data = json.load(data_file)
kalt, heiz, warm = [], [], []

def is_shared (zimmer):
    shared = Counter(list(data['Mitbewohnis'].values()))
    return shared[zimmer]

with open(output, 'w') as writer:
    gem_fläche = data["Totals"]["Gemeinschaftsfläche"]
    tot_zimmer_fläche = sum(list(data['Pro_zimmer'].values()))
    
    gem = gem_fläche/len(data["Mitbewohnis"])
    bet = data["Pro_person"]["Betriebskosten"]
    zus = data["Pro_person"]["Zusatzkosten"]
    puf = data["Pro_person"]["Puffer"]
    ext = data["Pro_person"]["Extra"]

    heiz_kost = data["Kosten"]["Heizung"]
    sqm_kost = data["Kosten"]["Fläche"] # cost per sqm
    gem_kost = round(gem * sqm_kost, 2)

    writer.write(f'''## WG Kosten

                \nKost der Gemeinschaftsfläche: €{sqm_kost}
                \nKost der Heizung per sqm: €{heiz_kost}

                \n| Mitbewohni | Zimmer | Fläche | Kalt | Heizung | Sonst | Warm |\n| --- | --- | --- | --- | --- | --- | --- |''')
    
    for name in data["Mitbewohnis"].keys():
        zimmer = data['Mitbewohnis'][name] # rommate name
        fläche = data['Pro_zimmer'][zimmer] # room name
        shared = is_shared(zimmer) # constant for shared rooms
        fast_warm = gem_kost + bet + zus + puf + ext # costs that stay the same for everybody
        k = round(gem_kost + fläche / shared * sqm_kost, 2) # kalt cost
        h = round(fläche * heiz_kost, 2) + round(gem * heiz_kost , 2)
        w = round(round(fläche / shared * sqm_kost, 2) + fast_warm + h, 2) # warm cost
        kalt.append(k)
        warm.append(w)
        heiz.append(h)

        writer.write(f'\n| {name} | {zimmer} | {fläche/shared} m2 | shared €{gem_kost} + room €{round(fläche / shared * sqm_kost, 2):.2f} = €{k:.2f} | shared €{round(gem * heiz_kost, 2):.2f} + room €{round(fläche * heiz_kost, 2):.2f} = €{h:.2f} | Betriebskosten €{bet:.2f} + Zusatzkosten €{zus:.2f} + Puffer €{puf:.2f} + Extra €{ext:.2f} = €{(bet + zus + puf + ext):.2f} | €{w:.2f} |')
    
    writer.write(f"\n| **Total** |  | **rooms {tot_zimmer_fläche} m2 + shared {gem_fläche} m2 = {tot_zimmer_fläche + gem_fläche} m2** | **€{sum(kalt):.2f}** | **€{sum(heiz):.2f}** | **€{((bet + zus + puf + ext) * len(data['Mitbewohnis'])):.2f}** | **€{sum(warm):.2f}** |")

    if sum(kalt) < data["Totals"]["Kalt"] - 5 or sum(kalt) > data["Totals"]["Kalt"] + 5:
        writer.write("\n\n\*WARNING: THE KALT COST HAS A DIFFERENCE BIGGER THAN €5.")
    if sum(heiz) < data["Totals"]["Heizung"] - 5 or sum(heiz) > data["Totals"]["Heizung"] + 5:
        writer.write("\n\n\*WARNING: THE HEIZUNG COST HAS A DIFFERENCE BIGGER THAN €5.")