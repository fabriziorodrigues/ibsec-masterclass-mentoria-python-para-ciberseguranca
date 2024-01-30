import socket

def scan_port(ip, port):
    try:
        # Cria um socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Define um tempo limite para a conexão
            s.settimeout(1)

            # Tenta conectar ao IP e porta
            result = s.connect_ex((ip, port))

            # Verifica se a conexão foi bem-sucedida (resultado 0)
            if result == 0:
                return True
            else:
                return False
    except:
        return False

# Endereço IP do alvo (exemplo)
target_ip = "192.168.1.1"

# Varre as portas de 1 a 1024
for port in range(1, 1025):
    if scan_port(target_ip, port):
        print(f"Porta {port} está aberta.")
