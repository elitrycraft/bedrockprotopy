import socket
import re
from pathlib import Path
from collections import defaultdict

def load_packet_definitions():
    yaml_path = Path("proto (1).yml")
    with yaml_path.open("r", encoding="utf-8") as f:
        content = f.read()
    
    packets = defaultdict(str)
    # Ищем все packet_* с !id
    pattern = r"^(packet_\w+):\s*\!id:\s*(0x[0-9a-fA-F]+|\d+)"
    matches = re.finditer(pattern, content, re.MULTILINE)
    
    for match in matches:
        packet_name = match.group(1)
        packet_id = match.group(2)
        packet_id = int(packet_id, 16) if packet_id.startswith("0x") else int(packet_id)
        packets[packet_id] = packet_name
    
    return dict(packets)

def parse_varint(data):
    result = 0
    shift = 0
    pos = 0
    while True:
        if pos >= len(data):
            raise ValueError("Incomplete varint")
        byte = data[pos]
        pos += 1
        result |= (byte & 0x7F) << shift
        shift += 7
        if not (byte & 0x80):
            return result, data[pos:]

def handle_packet(raw_data):
    if not raw_data or len(raw_data) < 2:
        return None
    
    try:
        length, remaining_data = parse_varint(raw_data)
        if len(remaining_data) < length:
            return None
        
        packet_id = remaining_data[0]
        packet_name = PACKET_DEFS.get(packet_id, f"UNKNOWN_PACKET_0x{packet_id:02x}")
        packet_content = remaining_data[1:length]
        
        return packet_name, packet_content
    except Exception as e:
        print(f"Packet parsing error: {e}")
        return None

def start_server(host="0.0.0.0", port=19132):
    global PACKET_DEFS
    PACKET_DEFS = load_packet_definitions()
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print(f"Server started on {host}:{port}")
        print("Known packet IDs:", sorted(PACKET_DEFS.items()))
        
        while True:
            try:
                data, addr = sock.recvfrom(4096)
                print(f"\nFrom {addr}:")
                print(f"Raw data (hex): {data.hex()}")
                
                result = handle_packet(data)
                if result:
                    name, content = result
                    print(f"Packet ID: 0x{data[1]:02x}")  # data[1] - первый байт после varint длины
                    print(f"Packet type: {name}")
                    print(f"Content (hex): {content.hex()}")
                else:
                    print("Invalid packet structure")
                    
            except KeyboardInterrupt:
                print("\nServer stopped")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    start_server()
