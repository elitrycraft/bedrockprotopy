# Bedrock Protocol Python (bedrockprotopy)

Python implementation of Minecraft Bedrock Edition protocol - ping servers, connect clients, and analyze packets.

## 📦 Installation

For development version:
```bash
pip install git+https://github.com/elitrycraft/bedrockprotopy.git
```

## 🚀 Current Status

### ✅ Implemented
- Full server ping functionality
- Server response parsing (MOTD, version, player count)
- Basic connection handshake

### 🛠 In Progress
- Packet construction system
- Connection stability improvements

### 📅 Planned
- Microsoft authentication
- Full client implementation
- World interaction

## 💻 Usage Examples

### Basic Server Ping
```python
from bedrockprotopy import ping_server

response = ping_server("play.example.com", 19132)
print(f"Server: {response['motd_line1']}")
print(f"Version: {response['version']}")
print(f"Players: {response['online_players']}/{response['max_players']}")
```
