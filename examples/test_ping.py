# import library
import bedrockprotopy

# ping local server
result = bedrockprotopy.ping(host="127.0.0.1", port=19132, timeout=5)

# print a result
print("Raw response:")
print(result["raw_response"])
print("")
print(f"""
server info:

motd_line1: {result.get('motd_line1')}
motd_line2: {result.get('motd_line2')}
protocol: {result.get('protocol')}
version: {result.get('version')}
online: {result.get('online_players')}
max_players: {result.get('max_players')}
""")
