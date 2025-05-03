from bottle import route, run, request, response, template, post, static_file, HTTPError
from parser import parse_v2 as parse
import os
import uuid
from datetime import datetime
import json

UPLOAD_DIR = "uploads"

heads_list = {
    "HFDTE": "Date",
    "HFPLT": "Pilot name",
    "HFCM2": "Secondary pilot",
    "HFGTY": "Glider type",
    "HFGID": "Registration",
    "HFDTM": "GPS date",
    "HFCID": "Competition ID",
    "HFCCL": "Club",
    "HFFTY": "Tow type",
    "HFFID": "Tow registration",
    "HFGPS": "GPS Device"
    
}

@route("/")
def index():
    return template("index")

@route("/static/<file>")
def static(file):
    return static_file(file, root="./static")

@post("/upload")
def upload():
    upload = request.files.get("myfile")
    
    if not upload.filename.lower().endswith('.igc'):
        raise HTTPError(400, "Please upload .igc files only!")
    
    filename = str(uuid.uuid4()) + ".igc"
    
    save_path = os.path.join(UPLOAD_DIR, filename)
    
    upload.save(save_path, overwrite=True)
    print(f"Ukládám soubor: {save_path}")
    
    
    parsed = parse(save_path)
    os.remove(save_path)
    print(f"Data z parseru: {parsed['heads']}")
    for i in list(parsed["heads"]):
        if i in heads_list:
            parsed["heads"][heads_list[i]] = parsed["heads"].pop(i)

    date_idk = datetime.strptime(parsed["heads"]["Date"], "%m%d%y")
    date_parsed = date_idk.strftime("%d/%m/%Y")
    parsed["heads"]["Date"] = date_idk.strftime("%d/%m/%Y")
    return template("main", heads=parsed["heads"], flight=json.dumps(parsed["flight"]))

run(host='192.168.0.45', port=8081, debug=True, reloader=True)
