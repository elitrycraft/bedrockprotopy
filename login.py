import socket
import struct
import time

def simple_connect(host: str, port: int = 19132):
    """Минимальная реализация подключения к локальному серверу"""
    MAGIC = bytes.fromhex("00ffff00fefefefefdfdfdfd12345678")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)

    try:
        # 1. Отправляем Ping
        ping = b'\x01' + struct.pack('>Q', int(time.time()*1000)) + MAGIC + struct.pack('>Q', 12345)
        sock.sendto(ping, (host, port))
        
        # 2. Получаем Pong
        data, _ = sock.recvfrom(2048)
        if data[0] != 0x1C:
            print("Ошибка: Сервер вернул неверный пакет")
            return False

        # 3. Отправляем Connection Request
        request = b'\x09' + struct.pack('>Q', 12345) + struct.pack('>Q', int(time.time()*1000)) + b'\x00'
        sock.sendto(request, (host, port))
        
        # 4. Ждём ответ
        data, _ = sock.recvfrom(2048)
        print(f"Ответ сервера: {data[:20].hex()}...")
        return True

    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    if simple_connect("127.0.0.1"):
        print("Подключение успешно!")
    else:
        print("Не удалось подключиться")
