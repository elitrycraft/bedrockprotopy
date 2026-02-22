import json

with open('packets.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

packets = data["packets"]

def get_packet_by_id(packet_id):
    for packet in packets:
        if packet['id'] == packet_id:
            return packet
    return None

def get_packet_by_name(packet_name):
    for packet in packets:
        if packet['name'] == packet_name:
            return packet
    return None
