import json

with open('packets.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

packets = data["packets"]
