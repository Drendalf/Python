import json
import os

root = os.path.dirname(__file__)

with open("config.json", "r", encoding="utf-8") as f:
    conf = json.load(f)

for dir_path in conf:
    ful = os.path.join(root, dir_path)
    os.makedirs(ful, exist_ok=True)
    for file in conf[dir_path]:
        with open(os.path.join(ful, file), "x", encoding="utf-8"):
            pass
