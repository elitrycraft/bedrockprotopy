# Bedrock Protocol Python (bedrockprotopy)

Python implementation of Minecraft Bedrock Edition protocol - ping servers, connect clients, and analyze packets.

## 📦 Installation

From git:
```bash
pip install git+https://github.com/elitrycraft/bedrockprotopy.git
```
From PyPI:
```bash
pip install bedrockprotopy
```

## 🚀 Current Status

### ✅ Implemented
- Full server ping functionality
- Server response parsing (MOTD, version, player count)

### 🛠 In Progress
- Packet send
- Player client functions
- Microsoft authentication
- World functions

## 💻 Usage Examples

### Basic Server Ping
```python
# import library
import bedrockprotopy

# ping local server
result = bedrockprotopy.ping(host="minescar.com", port=19132, timeout=5)

# print a result
print("Raw response:")
print(result["raw_response"])
print("")
print(f"""server info:

motd_line1: {result.get('motd_line1')}
motd_line2: {result.get('motd_line2')}
protocol: {result.get('protocol')}
version: {result.get('version')}
online: {result.get('online_players')}
max_players: {result.get('max_players')}""")
```
