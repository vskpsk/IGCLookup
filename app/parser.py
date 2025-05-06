import json

def convert_gps(gps):
    direction = gps[-1]
    sign = -1 if direction in ['S', 'W'] else 1
    gps_str = gps[:-1]

    degrees = int(gps[:-6])
    minutes = int(gps[-6:-4])
    seconds = int(gps[-4:-2])
    seconds += int(gps[-2]) * 0.1

    decimal = degrees + minutes / 60 + seconds / 3600
    return round(sign * decimal, 6)

def parse(igc_file):
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
                
                data["flight"][time] = {"lat": convert_gps(lat),"lon": convert_gps(lon), "fix": fix, "alt": alt, "gnss": gnss}
            
    print(data)            
    return data

def parse_v2(igc_file):
    return parse(igc_file)