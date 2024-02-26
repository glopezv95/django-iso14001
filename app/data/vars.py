from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent
VARS_PATH = BASE_DIR / 'static/app/json/vars.json'

with open(VARS_PATH, 'r', encoding='utf-8') as file:
    ccaa_dict = json.load(file)

    ccaa_list = []
    ccaa_list.extend([k for k in ccaa_dict.keys()])

    province_list = []
    province_list.extend([v for k in ccaa_dict for v in ccaa_dict[k]])