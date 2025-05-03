def parse(igc_file):
    print(f"Parsování souboru: {igc_file}")
    data = {"heads": {}, "flight": {}}
    with open(igc_file, 'r') as file:
        for line in file:
            if line[0] == "H":
                head = line[:5]
                if head == "HFDTE":
                    value = line[5:]
                    if value.endswith('\n'):
                        value = value[:-1]
                    data["heads"][head] = value
                else:
                    value = line.split(":")[1]
                    if value.endswith('\n'):
                        value = value[:-1]
                    data["heads"][head] = value
            elif line[0] == "B":
                time = line[1:7]
                lat = line[7:15]
                lon = line[15:24]
                fix = line[24]
                alt = line[25:30]
                gnss = line[30:35]
                
                data["flight"][time] = {"lat": lat, "lon": lon, "fix": fix, "alt": alt, "gnss": gnss}
                
    return data

def parse_v2(igc_file):
    print(">>> parse_v2 se spustil s:", igc_file)
    return parse(igc_file)

